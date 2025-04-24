import json, requests

with open("sample_data/patient1.json") as f:
    payload = json.load(f)

resp = requests.post("http://127.0.0.1:8000/input", json=payload)
print(resp.status_code)
print(resp.json())
