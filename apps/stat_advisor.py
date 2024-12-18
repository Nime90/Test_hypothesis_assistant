#NOT WORKING: IT STOPS WHEN SELECTING THE TEST
import streamlit as st
import pandas as pd
from utils.import_text_stat import all_stat_page#, import_text_stat_standard
from utils.recommend_test import recommend_test_nodata
from datetime import datetime
from dotenv import load_dotenv
import os

from utils.g_spread import save_log, load_cust_api

def run() -> None:
    Total_cost = 0.0
    st.title("Test of Hypothesis advisor :nerd_face: ")
    st.write("Ask me any question about test of hypothesis!")
    try:
        user_email = st.experimental_user.email
        user = user_email.split('@')[0]
        api_key = load_cust_api(user_email)
    except:
        user_email = 'dev'
        user = 'dev'
        api_key = None

    if api_key is None:
        st.write(f"Hi, Your email is not associated to valid account. Please contact nicolamenale90@gmail.com for help.")
    else:
        if  user_email is not None:
            st.write(f"Greetings, {user_email} 👋")
            api_key = load_cust_api(user_email)
        user_query = st.chat_input("Ask me questions about test of hypothesis")
        if user_query is not None:
            try:
                #source_text = import_text_stat('https://stats.oarc.ucla.edu/spss/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-spss/')
                source_text = all_stat_page()
                response, total_cost  = recommend_test_nodata(source_text, user_query,api_key)
                Total_cost = Total_cost + float(total_cost)
                st.write(response)

                #Save log of results
                current_datetime = datetime.now()
                results_interpretation = None
                log_info = ['stat_advisor.py',
                            str(current_datetime),
                            user,
                            user_email,
                            user_query,
                            response,
                            results_interpretation,
                            str(Total_cost).replace('.',',')]
                
                load_dotenv('env')
                credentials_json_str = str(os.getenv('credentials_json'))
                save_log(log_info, credentials_json_str)
            except:
                st.write("My apologies, but I'm not able to respond to this message.")
                st.write("Please ask me a question about a specific test of a hypothesis or describe your data so I can give you a recommendation.")

    if __name__ == "__main__":
        run()
