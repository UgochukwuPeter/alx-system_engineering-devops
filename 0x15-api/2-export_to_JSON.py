#!/usr/bin/python3
#  sends a request to the URL and export result
#  to a json file
""" script that fetches https://intranet.hbtn.io/status """

import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'

    reqEmployee = requests.get(url + sys.argv[1])
    reqTodos = requests.get(url + sys.argv[1] + '/todos/')
    jsonemp = reqEmployee.json()
    filename = str(jsonemp.get('id')) + ".json"
    tasks = {}
    tasks[jsonemp.get('id')] = []
    for todo in reqTodos.json():
        tasks[jsonemp.get('id')].append({"username": jsonemp.get('username'),
                                         "task": todo.get('title'),
                                         "completed": todo.get('completed')})

    with open(filename, 'w') as jsonfile:
        json.dump(tasks, jsonfile)
