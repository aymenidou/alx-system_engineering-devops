#!/usr/bin/python3
""" gather data from an API """
import requests
import sys
import json

if __name__ == '__main__':
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    users_response = requests.get(url_users)
    username = users_response.json().get('username')
    url_todos = "https://jsonplaceholder.typicode.com/todos/"
    todos_response = requests.get(url_todos).json()
    tasks = []
    for todo in todos_response:
        if (todo.get('userId') == int(sys.argv[1])):
            task_json = {
                'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': username
            }
            tasks.append(task_json)

    json_out = {
        sys.argv[1]: tasks
    }

    filename = sys.argv[1]+'.json'
    with open(filename, 'w') as file:
        json.dump(json_out, file)
