import streamlit as st


import functions

todos = functions.get_todos()  # abrimos el archivo todos.txt y lo guardamos como una lista de strings (un string por tarea).

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo.title())
    functions.write_todos(todos)

st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is to iuncrease your productivity')

for index, todo in enumerate(todos):  # importamos la lista de tareas desde nuestro archivo, de una en una en formato lista con bucle for:
    checkbox = st.checkbox(todo, key=todo) # checkbox es un diccionario con clave "todo" y el valor verdadero o falso (seleccionado o no).
    if checkbox: # si está seleccionado la clave todo...
        todos.pop(index)  # se elimina esa clave selecionada.
        functions.write_todos(todos)  # se sobreescribe en archivo todos.txt
        del st.session_state[todo]    # se elimina de ese diccinario checkbox la clave seleccionada.
        st.rerun()                    # se reinicia.

st.text_input(label='', placeholder='Enter a To-Do...', on_change=add_todo, key='new_todo')