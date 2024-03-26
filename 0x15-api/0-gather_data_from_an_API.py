#!/usr/bin/python3
# Write a Python script that, using this REST API, for a given
# employee ID, returns information about his/her Todo list progress.

import requests
import sys


if __name__ == "__main__":
    # Check if the script is provided with an employee ID as a command-line argument
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_ID = sys.argv[1]
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/users'
    url = f'{jsonplaceholder}/{employee_ID}'

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        employee_name = response.json().get('name')
        Todourl = f'{url}/todos'
        res = requests.get(Todourl)
        tasks = res.json()

        # Filter completed tasks
        done_tasks = [task for task in tasks if task.get('completed')]

        # Display the employee TODO list progress
        print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), len(tasks)))
        for task in done_tasks:
            print("\t{}".format(task.get('title')))
    else:
        # Display an error message if the request was not successful
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")