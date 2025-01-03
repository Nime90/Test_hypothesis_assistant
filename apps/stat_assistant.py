import streamlit as st
import pandas as pd
from utils.import_text_stat import import_text_stat
from utils.recommend_test import recommend_test 
from utils.interpret_results import interpret_results
from utils.run_test import run_test
from utils.find_dep_ind_var import find_dep_ind_var
from utils.g_spread import save_log, load_cust_api
from datetime import datetime
from dotenv import load_dotenv
import toml, os, json



def run() -> None:
    Total_cost = 0.0
    response = None
    results_interpretation = None

    st.title("Test of Hypothesys Assistant :brain: ")
    st.write("Please load here your data and ask me questions about it! ")

    user_email = st.experimental_user.email
    user = user_email.split('@')[0]
    api_key = load_cust_api(user_email)

    if  user_email is not None:
        st.write(f"Greetings, {user_email} 👋")
        api_key = load_cust_api(user_email)

    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read the Excel file into a DataFrame
        try:
            data = pd.read_excel(uploaded_file)
            source_text = import_text_stat()

            user_query = st.chat_input("What do you want to test from this data?")
            if user_query:
                response, total_cost = recommend_test(source_text, data, user_query, api_key)
                Total_cost = Total_cost + float(total_cost)
                st.write(response)
                
                if response:
                    test_name, dependent_variable, independent_variable,subject_varaible = find_dep_ind_var(response)
                    #debug script
                    #st.write('The most appropriate test is: ',test_name)
                    #for dv in dependent_variable:    st.write('Dependent variable(s)  : ',dv)
                    #for iv in independent_variable:  st.write('Independent variable(s): ',iv)

                    test_of_h = None
                    if test_name:
                        print('Running', test_name)
                        test_of_h = run_test(data,test_name,dependent_variable,independent_variable,subject_varaible)

                    if test_of_h  is not None:
                        # Assuming interpret_results is also defined
                        results_interpretation, total_cost = interpret_results(test_of_h , data, api_key)
                        Total_cost = Total_cost + float(total_cost)
                        st.write("Results Interpretation:")
                        st.write(results_interpretation)
        except:
            st.write('It seems that something is wrong with your dataset. Please review it.\n')
            st.write('You can ask for the help of our "Test of hypothesys advisor.\n')
            st.markdown("[Advisor (select me from the dropdown list on the left)](https://way2stat.streamlit.app/#test-of-hypothesis-advisor)")
            st.write('Remember to make sure to follow this template when uploading your data: \n')
            st.markdown("[Template](https://docs.google.com/spreadsheets/d/11FLvCX_dw0jsNJG7wBGPLAleQBrZJHV4/edit?usp=sharing&ouid=100261840869406723359&rtpof=true&sd=true)")
        
        if response is not None and results_interpretation is not None:
            current_datetime = datetime.now()
            log_info = ['stat_assistant.py',
                        str(current_datetime),
                        user,
                        user_email,
                        user_query,
                        response,
                        results_interpretation,
                        str(Total_cost).replace('.',',')]
            
            load_dotenv('.env')
            credentials_json_str = str(os.getenv('credentials_json')).replace('\n','\\n')
            save_log(log_info, credentials_json_str)
    
    if __name__ == "__main__":
        run()