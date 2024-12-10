import streamlit as st
import pandas as pd
import io


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
        "You can use the data belowas template"
    )

    file_content = pd.read_excel('Template.xlsx')
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        file_content.to_excel(writer, index=False, sheet_name='Sheet1')
        writer._save()
    excel_buffer.seek(0)

    st.download_button(
        label="Download Template File",
        data=excel_buffer,
        file_name='Template.xlsx',
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    run()
