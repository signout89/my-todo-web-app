import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    this_todo = st.session_state["new_todo"] + "\n"
    todos.append(this_todo)
    functions.write_todos(todos)

st.title('Марио/Боби сисък задачи')
st.subheader('Да не се чуди че няма къде да отбелязва')

st.write('Това е понеже Марио гледа да забравя.')
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key= todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Какво да се свърши вкарай и натисни Enter',
              on_change=add_todo, key='new_todo')
