#!/usr/bin/python3
"""
    using a REST API, for a given employee ID
    returns information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        userId = int(argv[1])
        url = "https://jsonplaceholder.typicode.com/users/"
        r = requests.get("{}/{}".format(url, userId))
        data = r.json()
        name = r.json().get("name")
        if name is not None:
            userTodos = requests.get("{}{}/todos".format(url, userId))
            userTodos = userTodos.json()
            taskNumber = len(userTodos)
            completedTasks = []
            for task in userTodos:
                if task.get("completed") is True:
                    completedTasks.append(task)
            taskCompletedNumber = len(completedTasks)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, taskCompletedNumber, taskNumber))
            for task in completedTasks:
                title = task.get("title")
                print("\t {}".format(title))
