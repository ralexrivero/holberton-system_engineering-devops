#!/usr/bin/python3
"""
    using a REST API, for a given employee ID
    returns information about his/her TODO list progress
"""

import requests
from sys import argv
userId = int(argv[1])

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/1/todos"
    r = requests.get(url)
    data = r.json()
    totalNumberOfTasks = len(data)
    numberOfDoneTasks = 0
    totalTasks = []
    for task in data:
        if task['userId'] == userId and task['completed'] is True:
            numberOfDoneTasks += 1
            totalTasks.append(task['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(userId, numberOfDoneTasks, totalNumberOfTasks))

    for task in totalTasks:
        print("\t{}".format(task))
