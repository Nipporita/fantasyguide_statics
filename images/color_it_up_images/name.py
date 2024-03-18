import hashlib
import json

def sha256(*args):
    return hashlib.sha256("".join(map(str, args)).encode()).hexdigest()

with open("index.json", 'r') as index:
    data = json.load(index)

for i in data["origin"]:
    print(i["character"], sha256(i["character"], i["type"]))