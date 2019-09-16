#!/usr/bin/python3
"""getting info from an api"""
import json
import requests as r
from sys import argv


if __name__ == "__main__":
    """exectute req to json"""

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos = r.get(todo_url).json()
    users = r.get(users_url).json()
    response = {}
    count = 0
    for user in users:
        user_todo = []
        temp = {}
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                count += 1
                temp.update({"task": todo.get("title")})
                temp.update({"completed": todo.get("completed")})
                temp.update({"username": user.get("username")})
                user_todo.append(temp)
                temp = {}
        response.update({user.get("id"): user_todo})
    name = "todo_all_employees.json"
    with open(name, mode='w') as json_f:
        json.dump(response, json_f)

