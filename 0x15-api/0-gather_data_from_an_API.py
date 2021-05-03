#!/usr/bin/python3
"""
script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    taskdone = 0
    user_id = argv[1]
    url_users = "https://jsonplaceholder.typicode.com/users?id="
    url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="

    resp = requests.get("{}{}".format(url_users, user_id)).json()
    name_user = resp[0].get('name')

    resp = requests.get("{}{}".format(url_tasks, user_id)).json()

    total_task = len(resp)

    title_list = []
    for task in resp:
        if str(task.get('completed')) == "True":
            taskdone += 1
            title_list.append(str(task.get('title')))

    print("Employee {} is done with tasks({}/{}):"
          .format(name_user, taskdone, total_task))

    for title in title_list:
        print("\t {}".format(title))
