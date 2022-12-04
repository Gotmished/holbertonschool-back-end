#!/usr/bin/python3
"""
Module to gather data from an API, and export in CSV format:
https://jsonplaceholder.typicode.com/
"""

import requests
import csv
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

    # Creating a csv file, determining format, and assigning data
    with open('{}.csv'.format(user_id), 'w', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=',',
                              quotechar='"', quoting=csv.QUOTE_ALL)
        for each_task in tasks:
            order_of_details = [users['id'], users['username'],
                                each_task['completed'], each_task['title']]
            csv_writer.writerow(order_of_details)


# Accepting user input as ID
if __name__ == '__main__':
    data_retrieval_export(int(argv[1]))
