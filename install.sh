#!/usr/bin/env bash
# Bootstrap the standalone Python installer, or use this checkout's copy.
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
  echo "EconFinHarness requires Python 3.9+ and Git." >&2
  exit 1
fi
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else "Python 3.9+ is required.")'

installer_directory=""
if [[ -n "${BASH_SOURCE[0]:-}" ]]; then
  installer_directory="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
fi
if [[ -n "$installer_directory" && -f "$installer_directory/install.py" && -f "$installer_directory/harness/VERSION" ]]; then
  exec python3 "$installer_directory/install.py" "$@"
fi

if ! command -v curl >/dev/null 2>&1; then
  echo "curl is required when running the downloaded bootstrap script." >&2
  exit 1
fi
installer_temporary="$(mktemp -d)"
trap 'rm -rf -- "$installer_temporary"' EXIT
curl --fail --silent --show-error --location \
  "https://raw.githubusercontent.com/Si1entPe661e/EconFinHarness/main/install.py" \
  --output "$installer_temporary/install.py"
python3 "$installer_temporary/install.py" "$@"
