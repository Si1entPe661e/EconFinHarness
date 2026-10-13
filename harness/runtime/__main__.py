"""CLI: python3 -m harness.runtime --root PROJECT --manifest task.json COMMAND."""
import argparse
import json
import sys
from pathlib import Path

from .dispatch import route
from .engine import Engine


def native_action(engine, args):
    """Host tool calls remain native; this CLI owns selection and durable receipts."""
    from .native import NativeDispatcher
    adapter = NativeDispatcher(engine, max_workers=args.workers,
                               available_agent_types=args.agent_types.split(","))
    action = args.native_action
    if action == "next":
        if not args.authorized:
            raise ValueError("Native delegation needs the user's authorization; pass --authorized only when it exists.")
        engine.run()
        requests = adapter.prepare(authorized=True)
        return {"execution": engine.status()["execution"], "dispatches": [
            {key: r[key] for key in ("task", "token", "role", "host_agent_type", "attempt", "tool_args", "context")}
            for r in requests]}
    if action == "status":
        return adapter.status()
    if action == "context":
        print(adapter.context(args.token)["prompt"])
        return None
    if action == "read":
        print(adapter.source_read(args.token, args.path, args.start, args.end)["text"])
        return None
    if action == "begin":
        result = adapter.begin(args.token)
    elif action == "bind":
        result = adapter.bind(args.token, args.native_id)
    elif action == "resolve":
        result = adapter.resolve(args.token, args.outcome, args.reason)
    else:
        path = Path(args.result_file)
        result = adapter.settle(args.token, args.native_id, args.terminal_state,
                                (path if path.is_absolute() else engine.root / path).read_text(encoding="utf-8"))
    return {key: result.get(key) for key in ("task", "token", "state", "native_id", "error")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--manifest", default="task.json")
    parser.add_argument("--state-dir", default=".harness")
    sub = parser.add_subparsers(dest="action", required=True)
    for name in ("run", "status", "ready", "events"):
        sub.add_parser(name)
    packet = sub.add_parser("packet"); packet.add_argument("task")
    done = sub.add_parser("complete"); done.add_argument("task"); done.add_argument("--token", required=True)
    recover = sub.add_parser("recover"); recover.add_argument("task"); recover.add_argument("--reason", required=True)
    evidence = sub.add_parser("evidence"); evidence.add_argument("record")
    routing = sub.add_parser("route"); routing.add_argument("capability")
    native = sub.add_parser("native", help="Select native host calls, bind observed handles and verify returns.")
    native.add_argument("--workers", type=int, default=2)
    native.add_argument("--agent-types", default="default", help="Comma-separated types actually advertised by this host.")
    actions = native.add_subparsers(dest="native_action", required=True)
    next_call = actions.add_parser("next"); next_call.add_argument("--authorized", action="store_true")
    actions.add_parser("status")
    for name in ("begin", "context", "bind", "read", "settle", "resolve"):
        action = actions.add_parser(name); action.add_argument("--token", required=True)
        if name in ("bind", "settle"):
            action.add_argument("--native-id", required=True)
        if name == "read":
            action.add_argument("--path", required=True)
            action.add_argument("--start", type=int, default=1)
            action.add_argument("--end", type=int)
        if name == "settle":
            action.add_argument("--terminal-state", choices=("completed", "failed", "interrupted"), required=True)
            action.add_argument("--result-file", required=True)
        if name == "resolve":
            action.add_argument("--outcome", choices=("not_started", "stopped"), required=True)
            action.add_argument("--reason", required=True)
    args = parser.parse_args()
    if args.action == "route":
        print(json.dumps(route(args.capability), indent=2)); return 0
    engine = Engine(args.root, args.manifest, args.state_dir)
    try:
        if args.action == "run": result = engine.run()
        elif args.action == "status": result = engine.status()
        elif args.action == "ready": result = engine.ready()
        elif args.action == "packet": result = engine.packet(args.task)
        elif args.action == "complete":
            engine.complete(args.task, args.token); result = engine.status()
        elif args.action == "recover":
            engine.recover(args.task, args.reason); result = engine.status()
        elif args.action == "evidence":
            path = Path(args.record)
            engine.record_evidence(json.loads((path if path.is_absolute() else engine.root / path).read_text()))
            result = engine.status()
        elif args.action == "native":
            result = native_action(engine, args)
            if result is None:
                return 0
        else:
            result = [dict(r) for r in engine.store.db.execute("SELECT * FROM events ORDER BY seq")]
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if args.action != "run" or result["execution"] == "succeeded" else 2
    finally:
        engine.close()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
