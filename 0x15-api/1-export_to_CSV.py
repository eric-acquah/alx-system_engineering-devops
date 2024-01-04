#!/usr/bin/python3

"""
Export employee's extracted TODO data from an api to CSV format

"""

import csv
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

filename = f"{uid}.csv"

# csv fieldnames = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]

with open(filename, 'w', newline="") as csvfile:
    csvWriter = csv.writer(csvfile)

    # Extract and write data into the csv file
    for task in todos:
        if task.get('userId') == uid:
            taskData = []
            taskData.append(str(uid))
            taskData.append(str(userName))
            taskData.append(str(task.get('completed')))
            taskData.append(str(task.get('title')))
            csvWriter.writerow(taskData)
