import json
from pathlib import Path


LEDGER_PATH = Path("ledger.jsonl")


def verify_ledger():
    if not LEDGER_PATH.exists():
        print("LEDGER: MISSING")
        return False

    with LEDGER_PATH.open("r") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print("LEDGER: EMPTY")
        return False

    legacy_count = 0

    for index, line in enumerate(lines, start=1):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            print(f"LEDGER: INVALID_JSON at line {index}")
            return False

        required = ["record_hash", "ts", "decision"]

        for field in required:
            if field not in entry:
                print(f"LEDGER: MISSING_FIELD {field} at line {index}")
                return False

        if "state_hash" not in entry:
            legacy_count += 1
            print(f"LEDGER: LEGACY_ENTRY at line {index}")

    print("LEDGER: VALID")

    if legacy_count:
        print(f"LEDGER: LEGACY_ENTRIES {legacy_count}")

    return True


if __name__ == "__main__":
    ok = verify_ledger()
    raise SystemExit(0 if ok else 1)
