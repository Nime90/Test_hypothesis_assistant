import streamlit as st
from apps import (
    stat_advisor,
    stat_assistant,
    stat_assistant_v1,
    data_cleaner,
    welcome
    )

pages = [
    {"title": "Welcome page", "function": welcome.run},
    {"title": "Your test of hypothesis advisor", "function": stat_advisor.run},
    {"title": "Your trusted data cleaner", "function": data_cleaner.run},
    {"title": "Your test of hypothesis assistant", "function": stat_assistant.run},
#    {"title": "Your test of hypothesis assistant_dev", "function": stat_assistant_v1.run},
]

st.set_page_config(page_title="Stat_Assistants", page_icon="🦾", layout="wide")
st.sidebar.title("Stat_Assistants 🦾")
st.sidebar.markdown("Test of Hypotesys helper. *Choose an app from the menu*")

page = st.sidebar.selectbox("App", pages, format_func=lambda page: page["title"])

page["function"]()
