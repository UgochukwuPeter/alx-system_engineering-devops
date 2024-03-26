#!/usr/bin/python3
#  sends a request to the URL and export result
#  to a json file
""" json file """

import json
import requests
import sys

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    url_todos = 'https://jsonplaceholder.typicode.com/todos/'

    req_users = requests.get(url_users)
    req_Todos = requests.get(url_todos)
    filename = "todo_all_employees.json"
    tasks = {}
    for user in req_users.json():
        tasks[user.get('id')] = []
        for todo in req_Todos.json():
            if todo.get('userId') == user.get('id'):
                tasks[user.get('id')].\
                      append({"username": user.get('username'),
                              "task": todo.get('title'),
                              "completed": todo.get('completed')})

    with open(filename, 'w') as jsonfile:
        json.dump(tasks, jsonfile)
