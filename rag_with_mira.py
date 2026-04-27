import sys
import requests

def mira_verify(state):
    try:
        response = requests.post(
            "http://localhost:8000/verify",
            json=state,
            timeout=5
        )
        result = response.json()
        return result.get("decision") == "PASS"
    except Exception:
        return False  # fail-closed

def rag_pipeline(query):
    # simulated retrieval
    retrieved = {
        "data": f"Result for: {query}",
        # add proof if your API expects it
        # "proof": "valid-proof"
    }

    # MIRA gate (fail-closed)
    if not mira_verify(retrieved):
        print("MIRA FAIL — execution halted")
        sys.exit(1)

    print("MIRA PASS — proceeding")
    return retrieved["data"]

if __name__ == "__main__":
    result = rag_pipeline("test query")
    print("OUTPUT:", result)
