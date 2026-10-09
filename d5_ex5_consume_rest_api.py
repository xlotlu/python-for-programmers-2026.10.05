import requests
import rich


URL = "https://jsonplaceholder.typicode.com/todos"

def get_todos(url, completed=False):
    """
    Gets todos, and filters by completed (default False),
    completed=None returns all items.
    """

    response = requests.get(url)

    if completed is None:
        filter_completed = lambda item: True
    else:
        filter_completed = lambda item: item['completed'] == completed

    return [
        item
        for item in response.json()
        if filter_completed(item)
    ]

for item in get_todos(URL, None):
    rich.print(item)
