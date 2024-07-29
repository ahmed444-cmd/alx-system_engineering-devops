#!/usr/bin/python3
""" A script to retrieve the TODO lists of all employees and save them
to a file in JSON format.
"""
from json import dump
from requests import get
from sys import argv


def to_do_list(emp_id, user):
""" Send a request to the API for the employee's TODO list.
"""
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    params = {'userId': emp_id}
    tasks = get(url_todo, params=params).json()

    #  create list of dictionaries
    #  with info about each task
    task_list = []
    for task in tasks:
        task_list.append({"username": user,
                          "task": task.get('title'),
                          "completed": task.get('completed')})
    return {emp_id: task_list}


def get_employees_to_do_lists():
""" Send a request to the API for all employees and their TODO
lists, then save the data in JSON format.
"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    file_name = 'todo_all_employees.json'
    to_do_lists = {}
    users = get(url).json()

    for user in users:
        to_do_lists.update(to_do_list(user.get('id'),
                           user.get('username')))

    # open file in write mode and jsonify
    with open(file_name, 'w', encoding='utf8') as f:
        dump(to_do_lists, f)


if __name__ == '__main__':
    get_employees_to_do_lists()
