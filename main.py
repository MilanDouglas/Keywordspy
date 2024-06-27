import json

with open ("sample_json.json", "r") as f:
  new_data = json.load(f)

print(new_data)