#!/usr/bin/python3
"""
Module to gather data from an API, and export in JSON format:
https://jsonplaceholder.typicode.com/
"""

import csv
import json
import requests
from sys import argv


def data_retrieval_export():
    """Retrieving data from an API for export in JSON"""
    # Setting variable for users and to-dos with url of API
    users_list = 'https://jsonplaceholder.typicode.com/users/'
    task_list = 'https://jsonplaceholder.typicode.com/todos'

    # Requesting information, and converting to json format
    users = requests.get(users_list).json()
    tasks = requests.get(task_list).json()
    details_dict = {}

    # For each user, find all tasks by iteration, and create a dictionary
    for each_user in users:
        user_tasks = []
        for each_task in tasks:
            order_of_details = {"username": each_user['username'],
                                "task": each_task['title'],
                                "completed": each_task['completed']}
            user_tasks.append(order_of_details)
        id_key = each_user['id']
        # In the dictionary, for key=particular ID, associate tasks
        details_dict[id_key] = user_tasks

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(details_dict, file)


# Accepting user input as ID
if __name__ == '__main__':
    data_retrieval_export()
