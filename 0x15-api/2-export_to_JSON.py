#!/usr/bin/python3

"""
Export employee's extracted TODO data from an api to JSON format

"""

import csv
import json
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


# Extract data
userName = userName.get('username')

filename = f"{uid}.json"

# Format { "USER_ID": [{"task": "TASK_TITLE", "completed":
# TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

with open(filename, 'w') as jsonfile:

    # Extract and write data into the json file
    taskList = []
    for task in todos:
        if task.get('userId') == uid:
            taskData = {}
            taskData['task'] = task.get('title')
            taskData['completed'] = task.get('completed')
            taskData['username'] = userName
            taskList.append(taskData)

    userInfo = {f'{uid}': taskList}

    json.dump(userInfo, jsonfile)
