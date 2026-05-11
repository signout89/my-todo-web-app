def get_todos(filepath="todo.txt"):
    """Read the todo.txt file and return a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath="todo.txt"):
    """Write the list of todos to a file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

