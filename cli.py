import todo_function
import  time

now = time.strftime("Month: %b Date:%d Year: %Y     Time: %H:%M:%S")
print(f"{now}")
while True:
    user_decision = input("Choose an option: Add, Show, Edit, Complete, Exit: ")
    user_decision = user_decision.strip()
    user_decision = user_decision.lower()


    if user_decision.startswith("add"):
            todo= user_decision[4:]+'\n'
            todos = todo_function.todos_read()
            todos.append(todo) #storing user input on todos variable
            #file write
            todo_function.todos_write(todos_arg=todos)


    elif user_decision.startswith("show"):

        todos = todo_function.todos_read()
        # new_todo = [data.strip('\n') for data in todos]
        # for index, data in enumerate(new_todo):
        for index,data in enumerate(todos):
            data = data.strip('\n')
            row = f"{index + 1}={data}"  # no space its called fstrings
            print(row)

    elif user_decision.startswith("complete"):
        try:
            number = int(user_decision[9:])

            todos = todo_function.todos_read()
            index = number-1
            todo_to_remove =todos[index].strip('\n')   #name of one of the todos is stored here

            todos.pop(index)  #tobo is remove and ready for sending it to the main txt file
            todo_function.todos_write(todos_arg=todos)

            massage = f"{todo_to_remove.capitalize()} has been removed from the list"
            print(massage)

        except IndexError:
            print("This task is not exist , please try again")
            continue
        except ValueError:
            print("please enter number after the complete text")
            continue

    elif user_decision.startswith("edit"):
        try:

            number = int(user_decision[5:])
            number = number - 1

            todos = todo_function.todos_read()

            new_todo = input("Enter Replacement:")     # asking replacement from the user
            todos[number] = new_todo +'\n'           #replacing  the new data in todos that we read from the txt file

             #replacement already done in the code now todos have a new value , we need send the new value on the txt file

            todo_function.todos_write(todos_arg=todos)    #add the updated file on the txt files , whole list is update on the local file
            print("Success!")
        except ValueError:
            print("invalid user input, command should be in number")
            continue
        except IndexError:
            print("Please enter a valid number that is exist")

    elif user_decision.startswith("exit"):
        break
    else :
        print(f"{user_decision} Command is not invalid")


print("system closed")

