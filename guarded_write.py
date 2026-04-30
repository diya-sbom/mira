import requests
import sys

API = "http://127.0.0.1:8000/verify"

def verify(state):
    r = requests.post(API, json=state)
    return r.json()

def write_file(content):
    with open("output.txt", "w") as f:
        f.write(content)

state = {
    "data": "write request",
   
}

result = verify(state)

if result["decision"] != "PASS":
    print("BLOCKED: MIRA FAIL")
    sys.exit(1)

print("ALLOWED: writing file")
write_file("Hello from controlled execution")
