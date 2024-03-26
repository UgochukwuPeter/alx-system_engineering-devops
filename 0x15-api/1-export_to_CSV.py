#!/usr/bin/python3
# Using what you did in the task #0, extend
# your Python script to export data in the CSV format.

import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/users'
    url = jsonplaceholder + '/' + USER_ID
    response = requests.get(url)
    username = response.json().get('username')
    todo_url = url + '/todos'
    response = requests.get(todo_url)
    tasks = response.json()
    with open(USER_ID + '.csv', 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(USER_ID, username,
                                                task.get('completed'),
                                                task.get('title')))