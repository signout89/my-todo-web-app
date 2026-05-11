import streamlit as st
import functions

# Apply custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"].strip()
    if new_todo:
        todos.append(new_todo + "\n")
        functions.write_todos(todos)
    # Clear the input field after adding
    st.session_state["new_todo"] = ""


st.markdown("""
    <div class="header-container">
        <h1 class="main-title">📝 Марио/Боби сисък задачи</h1>
        <p class="subtitle">Да не се чуди че няма къде да отбелязва</p>
        <p class="note">Това е понеже Марио гледа да забравя.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="todo-container">', unsafe_allow_html=True)

if not todos:
    st.markdown('<p class="empty-state">🎉 Няма задачи! Почивай си.</p>', unsafe_allow_html=True)
else:
    for index, todo in enumerate(todos):
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.markdown(f'<div class="todo-item">✦ {todo.strip()}</div>', unsafe_allow_html=True)
        with col2:
            if st.button("✕", key=f"del_{index}", help="Изтрий задачата"):
                todos.pop(index)
                functions.write_todos(todos)
                del st.session_state[todo]
                st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.text_input(
    label="Какво да се свърши — вкарай и натисни Enter",
    on_change=add_todo,
    key="new_todo",
    placeholder="Нова задача..."
)
st.markdown('</div>', unsafe_allow_html=True)
