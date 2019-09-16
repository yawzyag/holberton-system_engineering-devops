#!/usr/bin/python3
"""getting info from an api"""
import json
import requests as r
from sys import argv


if __name__ == "__main__":
    """exectute req to json"""

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        int(argv[1]))
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        int(argv[1]))
    todos = r.get(todo_url).json()
    users = r.get(users_url).json()
    user = users.get("username")
    user_id = str(users.get("id"))
    response = {}
    user_todo = []
    temp = {}
    for todo in todos:
        temp.update({"task": todo.get("title")})
        temp.update({"completed": todo.get("completed")})
        temp.update({"username": user})
        user_todo.append(temp)
        temp = {}

    response = {user_id: user_todo}
    name = "{}.json".format(user_id)
    with open(name, mode='w') as json_f:
        json.dump(response, json_f)
