#!/usr/bin/python3
"""
Module to gather data from an API:
https://jsonplaceholder.typicode.com/
"""

import requests
from sys import argv


def data_retrieval(user_id):
    """Retrieving data from an API"""
    # Setting variable for users and to-dos with url of API
    users_list = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(user_id)
    task_list = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)

    # Requesting information, and converting to json format
    users = requests.get(users_list).json()
    tasks = requests.get(task_list).json()
    number_of_tasks = len(tasks)
    completed_tasks = 0

    # First line
    for each_task in tasks:
        if each_task['completed']:
            completed_tasks += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(users['name'], completed_tasks, number_of_tasks))

    # Second line and onward
    for each_task in tasks:
        if each_task['completed']:
            print('\t {}'.format(each_task['title']))


# Accepting user input as id
if __name__ == '__main__':
    data_retrieval(int(argv[1]))
