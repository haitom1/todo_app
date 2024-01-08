import streamlit as st
import  todolist as td

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    td.write_todos(todos)


st.title("My todo App")
st.subheader("this is todo app")
#
# st.checkbox("Buy somthing new")


todos = td.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        td.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="todos",placeholder="add new todo...", on_change=add_todo, key='new_todo')
st.session_state