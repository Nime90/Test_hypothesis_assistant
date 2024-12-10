#NOT WORKING: IT STOPS WHEN SELECTING THE TEST
import streamlit as st
import pandas as pd
from utils.import_text_stat import all_stat_page#, import_text_stat_standard
from utils.recommend_test import recommend_test_nodata
from datetime import datetime
from dotenv import load_dotenv
import os

def save_log(log_info, credentials_json_str):
    import gspread
    import json
    # Parse the JSON string into a dictionary
    credentials_dict = json.loads(credentials_json_str)
    
    # Use the dictionary to authenticate
    gc = gspread.service_account_from_dict(credentials_dict)

    # Access a public Google Sheet by its URL
    sheet_url = "https://docs.google.com/spreadsheets/d/18aGkib26C8U7tiFZ86rMru9ZT65GaaNr0m9cIt3nk9Y/edit#gid=0"
    
    # Open the sheet by URL
    sheet = gc.open_by_url(sheet_url).sheet1

    # Append the log info
    sheet.append_row(log_info)
    
    print('log correctly saved')

def run() -> None:
    Total_cost = 0.0
    st.title("Test of Hypothesis advisor")
    st.write("Ask me any question about test of hypothesis!")
    user = st.context.headers.get('X-Streamlit-User')
    user_email = st.experimental_user.email
    if  user_email is not None:
        st.write(f"Greetings, {user_email} 👋")

    user_query = st.chat_input("Ask me questions about test of hypothesis")
    if user_query is not None:
        #source_text = import_text_stat('https://stats.oarc.ucla.edu/spss/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-spss/')
        source_text = all_stat_page()
        response, total_cost  = recommend_test_nodata(source_text, user_query)
        Total_cost = Total_cost + float(total_cost)
        st.write(response)

        #Save log of results
        current_datetime = datetime.now()
        results_interpretation = None
        log_info = [str(current_datetime),
                    user,
                    user_email,
                    user_query,
                    response,
                    results_interpretation,
                    str(Total_cost)]
        
        load_dotenv('env')
        credentials_json_str = str(os.getenv('credentials_json'))
        save_log(log_info, credentials_json_str)

    if __name__ == "__main__":
        run()
