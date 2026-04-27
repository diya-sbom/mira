from fastapi import FastAPI

app = FastAPI()

@app.post("/verify")
def verify(state: dict):
    if "proof" not in state:
        return {"decision": "FAIL"}
    return {"decision": "PASS"}
