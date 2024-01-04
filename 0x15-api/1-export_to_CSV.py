#!/usr/bin/python3
""" gather data from an API """
import csv
import requests
import sys


if __name__ == '__main__':
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    users_response = requests.get(url_users)
    if (users_response.status_code == 200):
        username = users_response.json().get('name')
        url_todos = "https://jsonplaceholder.typicode.com/todos/"
        todos_response = requests.get(url_todos).json()
        completed_tasks = 0
        tasks = 0
        task_desk = []
        filename = sys.argv[1] + '.csv'
        with open(filename, "w") as file:
            write = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
            for todo in todos_response:
                if (todo.get('userId') == int(sys.argv[1])):
                    row = [todo.get('userId'),
                           username,
                           str(todo.get('completed')),
                           todo.get('title')]
                    write.writerow(row)
