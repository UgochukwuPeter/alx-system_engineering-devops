#!/usr/bin/python3
#  sends a request to the URL and displays the value of
# the variable X-Request-Id in the response header
""" script that fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'

    reqEmployee = requests.get(url + sys.argv[1])
    reqTodos = requests.get(url + sys.argv[1] + '/todos/')

    jsonemp = reqEmployee.json()
    tasks = [key['completed'] for key in reqTodos.json()]
    print("Employee {} is done with tasks({}/{}):".format(jsonemp.get('name'),
          tasks.count(True), len(tasks)))
    for task in reqTodos.json():
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
