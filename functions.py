FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """Read todos from file and return a list."""
    try:
        with open(filepath, "r") as f:
            todos = f.readlines()
    except FileNotFoundError:
        todos = []
    return todos


def write_todos(todos, filepath=FILEPATH):
    """Write the list of todos back to the file."""
    with open(filepath, "w") as f:
        f.writelines(todos)
