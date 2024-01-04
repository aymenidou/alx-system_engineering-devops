#!/usr/bin/python3
""" gather data from an API """
import json
import requests


if __name__ == '__main__':
    url_users = "https://jsonplaceholder.typicode.com/users/"
    users_response = requests.get(url_users).json()
    url_todos = "https://jsonplaceholder.typicode.com/todos/"
    todos_response = requests.get(url_todos).json()
    json_out = {}

    for user in users_response:
        tasks = []
        for todo in todos_response:
            if (todo.get('userId') == user.get("id")):
                task_json = {
                    'username': user.get('username'),
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                }
                tasks.append(task_json)

        json_out[user.get("id")] = tasks

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(json_out, file)
