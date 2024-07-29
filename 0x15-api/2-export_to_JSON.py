#!/usr/bin/python3
"A Python script that saves data to a JSON file."
import json
import requests
import sys


def tasks_done(id):
    '''Script that exports an employee's TODO tasks to a JSON file.
Parameters:
employee_id: An integer representing the ID of the employee.'''

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    task_list = []

    for task in todos_json:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = employee_name
        task_list.append(task_dict)

    todos = {"{}".format(id): task_list}

    file_name = "{}.json".format(id)
    with open(file_name, "a") as fd:
        json.dump(todos, fd)


if __name__ == "__main__":
    tasks_done(sys.argv[1])
