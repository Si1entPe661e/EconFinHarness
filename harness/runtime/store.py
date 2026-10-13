"""Transactional checkpoints and append-only execution events in SQLite."""
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone


def now():
    return datetime.now(timezone.utc).isoformat()


class Store:
    def __init__(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, timeout=10)
        self.db.row_factory = sqlite3.Row
        self._savepoint = 0
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS tasks (
          id TEXT PRIMARY KEY, spec TEXT NOT NULL, state TEXT NOT NULL,
          attempts INTEGER NOT NULL DEFAULT 0, token TEXT, signature TEXT,
          outputs TEXT, error TEXT, prior_outputs TEXT);
        CREATE TABLE IF NOT EXISTS events (
          seq INTEGER PRIMARY KEY AUTOINCREMENT, at TEXT NOT NULL,
          task TEXT, action TEXT NOT NULL, detail TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS evidence (
          id TEXT PRIMARY KEY, record TEXT NOT NULL);
        """)
        if "prior_outputs" not in {r[1] for r in self.db.execute("PRAGMA table_info(tasks)")}:
            self.db.execute("ALTER TABLE tasks ADD COLUMN prior_outputs TEXT")
            self.db.commit()

    @contextmanager
    def transaction(self):
        # Reserve the writer before inspecting state, not only at the first UPDATE.
        nested = self.db.in_transaction
        self._savepoint += 1
        marker = "fh_savepoint_" + str(self._savepoint)
        self.db.execute("SAVEPOINT " + marker if nested else "BEGIN IMMEDIATE")
        try:
            yield
            if nested:
                self.db.execute("RELEASE SAVEPOINT " + marker)
            else:
                self.db.commit()
        except BaseException:
            if nested:
                self.db.execute("ROLLBACK TO SAVEPOINT " + marker)
                self.db.execute("RELEASE SAVEPOINT " + marker)
            else:
                self.db.rollback()
            raise

    def event(self, task, action, detail):
        self.db.execute("INSERT INTO events(at,task,action,detail) VALUES (?,?,?,?)",
                        (now(), task, action, json.dumps(detail, ensure_ascii=False)))

    def rows(self):
        return {r["id"]: dict(r) for r in self.db.execute("SELECT * FROM tasks")}

    def update(self, task, **fields):
        allowed = {"spec", "state", "attempts", "token", "signature", "outputs", "error", "prior_outputs"}
        if not fields.keys() <= allowed:
            raise ValueError("Unknown state field.")
        self.db.execute("UPDATE tasks SET " + ",".join(k + "=?" for k in fields) + " WHERE id=?",
                        list(fields.values()) + [task])

    def close(self):
        self.db.close()
