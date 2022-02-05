#!/usr/bin/python3
"""
export data in json format
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()
    userj = {}
    for user in users:
        userId = user.get("id")
        username = user.get("username")
        todos = requests.get("{}users/{}/todos".format(url, userId)).json()
        t = [{"username": username,
              "task": t.get("title"),
              "completed": t.get("completed"),
              } for t in todos]
        userj[userId] = t
    with open("todo_all_employees.json", 'w') as filejs:
        json.dump(userj, filejs)
