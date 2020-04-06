import json
import os

with open(os.environ['GITHUB_EVENT_PATH']) as f:
    data = json.load(f)

print(data)
