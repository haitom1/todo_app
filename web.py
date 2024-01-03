import streamlit as st
import  todolist as td

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    td.write_todos(todos)


st.title("My todo App")
st.subheader("this is todo app")
#
# st.checkbox("Buy somthing new")


todos = td.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="todos",placeholder="add new todo...", on_change=add_todo, key='new_todo')
st.session_state