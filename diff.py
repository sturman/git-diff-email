import json
import os

import requests

with open(os.environ['GITHUB_EVENT_PATH']) as f:

    data = json.load(f)
    print(data)
    commits = data['commits']
    for commit in commits:
        r = requests.get(commit['url'])
        print(r.text)
