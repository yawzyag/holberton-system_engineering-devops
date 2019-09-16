#!/usr/bin/python3
"""getting info from an api"""
import csv
import requests as r
from sys import argv


if __name__ == "__main__":
    """exectute req to csv"""
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos = r.get(todo_url)
    users = r.get(users_url)
    done, total, tasks, compl = 0, 0, [], []
    for x in todos.json():
        if x.get("userId") == int(argv[1]):
            total += 1
            if x.get("completed") is True:
                done += 1
            tasks.append(x.get("title"))
            compl.append(x.get("completed"))
    for y in users.json():
        if y.get("id") == int(argv[1]):
            user = y.get("username")
            my_id = y.get("id")

    actual, to_csv, items = 0, [], []
    for task in tasks:
        items.append(my_id)
        items.append(user)
        items.append(compl[actual])
        items.append(task)
        to_csv.append(items)
        items = []
        actual += 1

    csv.register_dialect('myDialect',
                         quoting=csv.QUOTE_ALL,
                         skipinitialspace=True)
    name = "{}.csv".format(argv[1])
    with open(name, mode='w') as employee_file:
        task_writer = csv.writer(employee_file, dialect='myDialect')
        for info in to_csv:
            task_writer.writerow(info)
