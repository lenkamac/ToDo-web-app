import streamlit as st
import functions
from PIL import Image

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


image = Image.open('files/robot-1470108_640.png')

with open('files/custom.css') as file:
    design = file.read()

st.markdown(f'<style>{design}</style>', unsafe_allow_html=True)

st.write("<h1 class='my_h1'>To-Do App</h1>", unsafe_allow_html=True)

st.write("<p class='my_p'>This app is to increase your productivity.</p>",
         unsafe_allow_html=True)

todos = functions.get_todos()


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='enter', placeholder='Add new todo...', on_change=add_todo,
              label_visibility='hidden', key='new_todo')

st.image(image, use_column_width=True)
