import streamlit as st
import pandas as pd

def run():
    st.title("Welcome to the Test of Hypothesis app! :wave:")
    st.header(":bar_chart: Please follow these steps to ensure good quality for your test of Hypothesis!")

    st.subheader("1. Test of Hypothesis Advisor :nerd_face:")
    st.text("This is your first step!.\n" 
            "Please ask  your advisor all queries pertaining to hypothesis testing.\n"
            "If you explain your data and your idea, they will help you properly defining a test of hypothesis \n"
            "and also what test to use to validate your hypotesis!\n"
            "The Advisor will be happy to help recommend you ways to fix your data as well(if you need)")
    
    st.subheader("2. Mister Cleaner :bookmark_tabs:")
    st.text(
        "Once you properly defined your test of hypothesis, you can ask Mr Clean to clean your data for you!\n"
        "Mr Clean will give you an explanation on what it did to the data and will provide you with a clean csv file"
    )

    st.subheader("3. Test of Hypothesis Assistant :brain:")
    st.text(
        "This application enables the loading of data and the formulation of a test of hypothesis.\n"
        "The assistant will perform the test and provide an interpretation of the results.\n"
        "Prior to loading the dataset, it is essential to ensure that the data is clean and prepared for the test.\n"
        'If necessary, guidance can be sought from the "Test of Hypothesis Advisor" or "Mr Clean". \n'
        "The file below can be used as a template.\n"

    )
    st.markdown("[Template](https://docs.google.com/spreadsheets/d/11FLvCX_dw0jsNJG7wBGPLAleQBrZJHV4/edit?usp=sharing&ouid=100261840869406723359&rtpof=true&sd=true)")

if __name__ == "__main__":
    run()
