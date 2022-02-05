#!/usr/bin/python3
"""
export to json
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        userId = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get("{}users/{}".format(url, userId)).json()
        username = user.get('username')
        todos = requests.get("{}users/{}/todos".format(url, userId)).json()
        t = [{"task": t.get("title"),
              "completed": t.get("completed"),
              "username": username} for t in todos]
        bj = {}
        bj[userId] = t
        with open("{}.json".format(userId), 'w') as filejs:
            json.dump(bj, filejs)
    else:
        print("usage: {} <user_id>".format(argv[0]))
        exit(1)
