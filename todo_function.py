file_location = "store.txt"

def todos_read(filepath=file_location):
    """
    Reads the list of todos from the text file and return to-dos so this data
    can be used in to-dos write function.
    """

    with open(filepath, 'r') as file_local:  # with & as is a content manager for file handling
        todos_local = file_local.readlines()
        return  todos_local

def todos_write(todos_arg,filepath=file_location):
    """ write to-do on the to-dos txt file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("I amm running")
