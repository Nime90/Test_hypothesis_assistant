import streamlit as st
import pandas as pd

def run():
    st.title("Welcome to the Test of Hypothesis app! :wave:")
    st.header(":toolbox: Our Services")
    st.subheader("Test of Hypothesis Advisor")
    st.text("This tool is designed to address all queries pertaining to hypothesis testing.")

    st.subheader("Test of Hypothesis Assistant")
    st.text(
        "This application enables the loading of data and the formulation of a test of hypothesis.\n"
        "The assistant will perform the test and provide an interpretation of the results.\n"
        "Prior to loading the dataset, it is essential to ensure that the data is clean and prepared for the test.\n"
        'If necessary, guidance can be sought from the "Test of Hypothesis Advisor". \n'
        "The file below can be used as a template.\n"

    )
    st.markdown("[Template](https://docs.google.com/spreadsheets/d/11FLvCX_dw0jsNJG7wBGPLAleQBrZJHV4/edit?usp=sharing&ouid=100261840869406723359&rtpof=true&sd=true)")

if __name__ == "__main__":
    run()
