import json
from pathlib import Path
from verify_output import verify_receipt


ATTACKS = [
    ("ATTACK-001", "adversarial/missing_field.json", False),
    ("ATTACK-002", "adversarial/invalid_decision.json", False),
    ("ATTACK-003", "adversarial/hash_tampered.json", False),
    ("ATTACK-005", "adversarial/truncated.json", False),
]


def run_attack(attack_id, path, expected):
    print(f"{attack_id}: {path}")

    try:
        actual = verify_receipt(path)
    except Exception as exc:
        print(f"RESULT: BLOCK")
        print(f"ERROR: {type(exc).__name__}")
        actual = False

    if actual == expected:
        print("EXPECTED: BLOCK")
        print("ACTUAL: BLOCK")
        print("STATUS: PASS\n")
        return True

    print("STATUS: FAIL\n")
    return False


if __name__ == "__main__":
    results = []

    for attack_id, path, expected in ATTACKS:
        results.append(run_attack(attack_id, path, expected))

    if not all(results):
        raise SystemExit(1)

    print("ADVERSARIAL CORPUS: ALL PASS")
