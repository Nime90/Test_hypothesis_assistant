import streamlit as st
import pandas as pd
import io
import subprocess
import sys

def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install_package('xlsxwriter')

def run():
    st.title("Welcome to the Test of Hypothesis app! :wave:")
    st.header(":toolbox: Our Services")
    st.subheader("Test of Hypothesis Advisor")
    st.text("Tool that is ready to answer to all your question about hypothesis testing")

    st.subheader("Test of Hypothesis Assistant")
    st.text(
        "This app allowes you to load your data and formulate your test of hypothesis.\n"
        "The assistant will perform the test and interpret the results for you!\n"
        "Before loading your dataset, please make sure that data is clean and ready\nfor your test (maybe ask advice to the Advisor).\n"
        "You can use the file below as template: \n"
    )
    st.markdown("[Template](https://docs.google.com/spreadsheets/d/11FLvCX_dw0jsNJG7wBGPLAleQBrZJHV4/edit?usp=sharing&ouid=100261840869406723359&rtpof=true&sd=true)")

if __name__ == "__main__":
    run()
