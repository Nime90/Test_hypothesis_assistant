#NOT WORKING: IT STOPS WHEN SELECTING THE TEST
import streamlit as st
import pandas as pd
from utils.import_text_stat import import_text_stat
from utils.recommend_test import recommend_test 
from utils.interpret_results import interpret_results
from utils.run_test import run_test
from utils.find_dep_ind_var import find_dep_ind_var

from streamlit.web.server.websocket_headers import _get_websocket_headers
from datetime import datetime


# Get the current date and time

def get_authenticated_user_email() -> str:
    """Extracts the email of the authenticated user from websocket headers."""
    headers = _get_websocket_headers()
    email = headers.get("X-Goog-Authenticated-User-Email")

    if email:
        return email
    return "dev"

def save_log(log_info):
    import gspread

    # Access a public Google Sheet by its URL
    sheet_url = "https://docs.google.com/spreadsheets/d/18aGkib26C8U7tiFZ86rMru9ZT65GaaNr0m9cIt3nk9Y/edit#gid=0"
    gc = gspread.service_account('credentials.json')  # No need to pass credentials for public sheets

    # Open the sheet by URL
    sheet = gc.open_by_url(sheet_url).sheet1

    sheet.append_row(log_info)
    
    print('log_correctly saved')

st.title("Hypothesis Testing Assistant")
user = st.context.headers.get('X-Streamlit-User')
user_email = st.experimental_user.email
st.write(st.context.headers.get('X-Streamlit-User'))
if  user_email is not None:
    st.write(user_email)

#st.write(f"Greetings, {email} 👋")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read the Excel file into a DataFrame
    data = pd.read_excel(uploaded_file)
    source_text = import_text_stat()

    user_query = st.chat_input("What do you want to test from this data?")
    if user_query:
        response = recommend_test(source_text, data, user_query)
        st.write(response)
        
        if response:
            test_name, dependent_variable, independent_variable = find_dep_ind_var(response)
            #debug script
            #st.write('The most appropriate test is: ',test_name)
            #for dv in dependent_variable:    st.write('Dependent variable(s)  : ',dv)
            #for iv in independent_variable:  st.write('Independent variable(s): ',iv)

            test_of_h = None
            if test_name:
                print('Running', test_name)
                test_of_h = run_test(data,test_name,dependent_variable,independent_variable)

            if test_of_h  is not None:
                # Assuming interpret_results is also defined
                results_interpretation = interpret_results(test_of_h , data)
                st.write("Results Interpretation:")
                st.write(results_interpretation)

                current_datetime = datetime.now()
                log_info = [str(current_datetime),
                            user,
                            user_email,
                            user_query,
                            response,
                            results_interpretation]
                save_log(log_info)
