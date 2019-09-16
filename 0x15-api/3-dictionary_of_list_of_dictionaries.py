#!/usr/bin/python3
"""getting info from an api"""
import json
import requests as r
from sys import argv


if __name__ == "__main__":
    """exectute all req to json"""
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    users = r.get(users_url).json()
    todos = r.get(todo_url).json()

    response, user_todo, temp, user_id = {}, {}, {}, {}

    for user in users:
        response[user.get("id")] = []
        user_todo[user.get("id")] = user.get("username")
        user_id[user.get("id")] = user.get("id")

    for todo in todos:
        if todo.get("userId") == user_id.get(todo.get("userId")):
            temp.update({"username": user_todo.get(todo.get("userId"))})
            temp.update({"task": todo.get("title")})
            temp.update({"completed": todo.get("completed")})
        response.get(todo.get("userId")).append(temp)
        temp = {}

    name_json = "todo_all_employees.json"
    with open(name_json, 'w') as j_file:
        json.dump(response, j_file)
