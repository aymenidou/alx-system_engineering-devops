#!/usr/bin/python3
""""""
import requests
import sys


if __name__ == '__main__':
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    users_response = requests.get(url_users)
    username = users_response.json().get('name')
    url_todos = "https://jsonplaceholder.typicode.com/todos/"
    todos_response = requests.get(url_todos).json()
    completed_tasks = 0
    tasks = 0
    task_desk = []
    for todo in todos_response:
        if (todo.get('userId') == int(sys.argv[1])):
            tasks += 1
            if (todo.get('completed') == True):
                completed_tasks += 1
                task_desk.append(todo.get('title'))
    print("Employee {} is done with tasks ({}/{}):".format(username,
          completed_tasks, tasks))
    for i in task_desk:
        print("\t {}".format(i))
