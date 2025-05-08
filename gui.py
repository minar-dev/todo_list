import todo_function
import FreeSimpleGUI as sg

sg.theme('GreenMono')
label = sg.Text('Type in in todos')
input_box = sg.InputText(tooltip='enter todo here', key="todo")
list_box = sg.Listbox(values=todo_function.todos_read(), key='todos', enable_events= True, size=[45,10])
edit_button = sg.Button('edit')

add = sg.Button('add')
complete_button = sg.Button('complete')
exit_button = sg.Button('Exit')

window = sg.Window( 'Welcome to todos',[[label],[input_box,add],
                                        [list_box,edit_button,complete_button],
                                        [exit_button]],font=('', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:

        case "add":
            todos = todo_function.todos_read()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            todo_function.todos_write(todos)
            window['todos'].Update(values=todos)

        case "edit":
            try:
                todo_to_edit = values['todos'][0] #selecting the to - do you want edit
                new_todo = values['todo'] # take the replacement

                todos = todo_function.todos_read()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                todo_function.todos_write(todos)
                window['todos'].Update(values=todos)
            except IndexError:
                sg.popup('Select an Item first',font=('', 20))

        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = todo_function.todos_read()
                todos.remove(todo_to_complete)
                todo_function.todos_write(todos)
                window['todos'].update(values=todos) # we have new list after complete this is need for update the list
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Select an Item first', font=('', 20))



        case "todos":
            window['todo'].Update(value=values['todos'][0]) #[0] this used collect selected on from the list

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break
print('bye')
window.close()


