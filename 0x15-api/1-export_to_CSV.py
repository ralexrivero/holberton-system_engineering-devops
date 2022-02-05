#!/usr/bin/python3
"""
export data in the CSV format
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        userId = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        r = requests.get("{}users/{}".format(url, userId))
        username = r.json().get('username')
        if username is not None:
            todos = requests.get("{}users/{}/todos".format(url, userId)).json()
        with open("{}.csv".format(userId), 'w', newline='') as csvfile:
            writeFile = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                writeFile.writerow([int(userId),
                                   username,
                                   task.get('completed'),
                                   task.get('title')])
