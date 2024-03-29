#!/usr/bin/python3
"""
Script to export data in the CSV format
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    task_done = 0
    user_id = argv[1]
    url_users = "https://jsonplaceholder.typicode.com/users?id="
    url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="

    resp = requests.get("{}{}".format(url_users, user_id)).json()
    user_name = resp[0].get('username')

    resp = requests.get("{}{}".format(url_tasks, user_id)).json()

    title_list = []

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        my_writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)

        for task in resp:
            task_status = task.get('completed')
            task_title = task.get('title')
            my_writer.writerow([user_id, user_name, task_status, task_title])
