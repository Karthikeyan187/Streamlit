import streamlit as st
from streamlit_option_menu import option_menu

st.title('My Project')
with st.sidebar:
    selected = option_menu(
        menu_title="Fitness Tracker",
        options=["Abstract", "Task", "System reuirements", "Modules"],
    )