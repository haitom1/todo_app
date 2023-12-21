import PySimpleGUI as sg
import todolist as td
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")


window = sg.Window('My to-do app', layout=[[label],
                    [input_box, add_button]],
                    font=('Helvetica',10))

#close the window
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = td.get_todos()
            print(todos)
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            print(todos)
            td.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()