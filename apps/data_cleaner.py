#NOT WORKING: IT STOPS WHEN SELECTING THE TEST
import streamlit as st
import pandas as pd
from utils.import_text_stat import import_text_stat
from utils.recommend_test import recommend_test 
from utils.interpret_results import interpret_results
from utils.run_test import run_test
from utils.find_dep_ind_var import find_dep_ind_var
from utils.fix_my_data_stable import fix_my_data_stable
from utils.g_spread import save_log, load_cust_api

from datetime import datetime
from dotenv import load_dotenv
import toml, os, json
load_dotenv('.env')


def run() -> None:
    Total_cost = 0.0
    st.title("Mister Cleaner :bookmark_tabs:")
    st.write("Please load here your data and your test of hypothesys and let me clean it for you! ")

    user_email = st.experimental_user.email
    user = user_email.split('@')[0]
    api_key = load_cust_api(user_email)

    if  user_email is not None:
        st.write(f"Greetings, {user_email} 👋")

    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read the Excel file into a DataFrame
        try:
            data = pd.read_excel(uploaded_file)
            source_text = import_text_stat()

            user_query = st.chat_input("What is your hypothesys?")
            if user_query:
                response, total_cost = recommend_test(source_text, data, user_query,api_key)
                Total_cost = Total_cost + float(total_cost)
                st.write(response)
                
                if response:
                    test_name, dependent_variable, independent_variable = find_dep_ind_var(response)
                    #debug script
                    #st.write('The most appropriate test is: ',test_name)
                    #for dv in dependent_variable:    st.write('Dependent variable(s)  : ',dv)
                    #for iv in independent_variable:  st.write('Independent variable(s): ',iv)

                    if test_name:
                        st.write('openinig: ',test_name)
                        with open('Tests/'+str(test_name), 'r') as file:
                            test_of_hypothesys_content = file.read()

                        response_exp, total_cost = fix_my_data_stable(data, test_of_hypothesys_content, user_query, api_key)
                        Total_cost = Total_cost + float(total_cost)
                        if response_exp is not None:
                            st.write(response_exp)
                        
                        try:
                            from utils.fix_my_data_temp import fix_my_data_temp
                            st.session_state.data_clean = fix_my_data_temp(data)
                            st.write(st.session_state.data_clean)

                            if 'data_clean' in st.session_state and st.session_state.data_clean is not None:
                                csv = st.session_state.data_clean.to_csv(index=False).encode('utf-8')
                                st.download_button(
                                    label="Download data_clean as CSV",
                                    data=csv,
                                    file_name="data_clean.csv",
                                    mime="text/csv"
                                    )
                        except : 
                            st.write("'Sorry, I am still a beta version: I wasn't able to clean your results. Please try again.")

                current_datetime = datetime.now()
                log_info = ['data_Cleaner.py',
                            str(current_datetime),
                            user,
                            user_email,
                            user_query,
                            response,
                            '',
                            str(Total_cost).replace('.',',')]
                
                load_dotenv('env')
                credentials_json_str = str(os.getenv('credentials_json'))
                save_log(log_info, credentials_json_str)
        except:
            st.write('Sorry, I am still a beta version: I am not able to figure out how to fix your data for the hypothesys you want to test.\n')
            st.write('You can ask for the help of our "Test of hypothesys advisor.\n')
            st.markdown("[Advisor (select me from the dropdown list on the left)](https://way2stat.streamlit.app/#test-of-hypothesis-advisor)")
            st.write('The Advisor will help you following this template to test your hypothesis: \n')
            st.markdown("[Template](https://docs.google.com/spreadsheets/d/11FLvCX_dw0jsNJG7wBGPLAleQBrZJHV4/edit?usp=sharing&ouid=100261840869406723359&rtpof=true&sd=true)")
    
    if __name__ == "__main__":
        run()