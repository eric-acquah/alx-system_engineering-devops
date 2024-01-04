#!/usr/bin/python3

"""
Gather data about an employee's todo list progress in a given API

"""

import requests
import sys


# Get employeeId
try:
    uid = int(sys.argv[1])
except Exception:
    print("Usage: ./0-gather_data_from_an_API.py <EMPLOYEE_ID>")

# Fetch for the todos
response1 = requests.get('https://jsonplaceholder.typicode.com/todos/')


# Fetch for name of employee
response2 = requests.get(f'https://jsonplaceholder.typicode.com/users/{uid}')


# Deserialize json object for extraction
userName = response2.json()
todos = response1.json()

# Initailize counters
taskCount = 0
taskDone = 0

# Extract data
userName = userName.get('name')

taskTitle = []  # set list to contain title of completed task

for task in todos:
    if task.get('userId') == uid:
        taskCount += 1
        if task.get('completed') is True:
            taskDone += 1
            taskTitle.append(task.get('title'))


# Print result to stdout
print(f"Employee {userName} is done with tasks({taskDone}/{taskCount}):")

for todo in taskTitle:
    print(f"\t {todo}")
