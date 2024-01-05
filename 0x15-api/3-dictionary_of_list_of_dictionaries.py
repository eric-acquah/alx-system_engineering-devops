#!/usr/bin/python3

"""
Export employee's extracted TODO data from an api to JSON format

"""

import json
import requests
import sys


# Fetch for the todos
response1 = requests.get('https://jsonplaceholder.typicode.com/todos/')


# Fetch for name of employee
response2 = requests.get(f'https://jsonplaceholder.typicode.com/users/')

# Deserialize json object for extraction
users = response2.json()
todos = response1.json()


# Extract data

# Format { "USER_ID": [{"task": "TASK_TITLE", "completed":
# TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

userInfo = {}
for usr in users:  # Work within the context of one user per iteration
    uid = usr.get('id')
    taskList = []

    for task in todos:  # Extract todos specific to a particular user
        if task.get('userId') == uid:
            taskData = {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': usr.get('username')
            }

            taskList.append(taskData)

    userInfo[f'{uid}'] = taskList  # Each key-value pair represent user data

# create file and dump data into it
filename = "todo_all_employees.json"
with open(filename, 'w') as jsonfile:
    json.dump(userInfo, jsonfile)
