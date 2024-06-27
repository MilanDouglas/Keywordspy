import requests

with open ('../data/sample.txt', "r") as f:
  data = f.read()

print(data.splitlines())
