#!/usr/bin/python3
"""
Module to gather data from an API, and export in JSON format:
https://jsonplaceholder.typicode.com/
"""

import csv
import json
import requests
from sys import argv


def data_retrieval_export(user_id):
    """Retrieving data from an API for export in CSV"""
    # Setting variable for users and to-dos with url of API
    users_list = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(user_id)
    task_list = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)

    # Requesting information, and converting to json format
    users = requests.get(users_list).json()
    tasks = requests.get(task_list).json()
    list_of_details = {user_id: []}

    # Creating a csv file, determining format, and assigning data
    for each_task in tasks:
        order_of_details = {"task": each_task['title'], "completed":
                            each_task['completed'], "username":
                            users['username']}
        # list_of_details treated as a dictionary object
        list_of_details[user_id].append(order_of_details)
    with open('{}.json'.format(user_id), 'w', encoding='utf-8') as file:
        json.dump(list_of_details, file)


# Accepting user input as ID
if __name__ == '__main__':
    data_retrieval_export(int(argv[1]))
