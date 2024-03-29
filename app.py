import PySimpleGUI as sg
import todolist as td
import time
import os
# sg.theme('BluePurple')

if not os.path.exists("data.txt"):
    with open("data.txt" , "w") as file:
        pass
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
# add_button = sg.Button("Add", image_source="add.png")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="white", tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=td.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
window = sg.Window('My to-do app',
                    layout=[[clock],[label], [input_box, add_button],[list_box, edit_button, complete_button],[exit_button]],
                    font=('Helvetica',10))

#close the window
while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    # print((values['todos']))
    match event:
        case "Add":
            todos = td.get_todos()
            print(todos)
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            print(todos)
            td.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit =values['todos'][0]
                new_todo = values['todo']

                todos = td.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                td.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = td.get_todos()
                todos.remove(todo_to_complete)
                td.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break
window.close()