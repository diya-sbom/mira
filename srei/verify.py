def verify_reasoning(text):
    lowered = text.lower()

    if "sn2" in lowered and "tertiary carbon" in lowered:
        return {
            "decision": "FAIL",
            "failure": "MECHANISM_VIOLATION",
            "explanation": "SN2 mechanism asserted at a tertiary carbon. Steric hindrance prevents the mechanism from occurring."
        }

    return {
        "decision": "PASS",
        "failure": None,
        "explanation": "No defined reasoning-integrity violation detected."
    }


if __name__ == "__main__":
    sample = "SN2 substitution occurs at a tertiary carbon."
    print(verify_reasoning(sample))
