#NOT WORKING: IT STOPS WHEN SELECTING THE TEST
import streamlit as st
import pandas as pd
from utils.import_text_stat import import_text_stat
from utils.recommend_test import recommend_test 
from utils.interpret_results import interpret_results
from utils.run_test import run_test
from utils.find_dep_ind_var import find_dep_ind_var, find_dep_ind_var_0
from utils.fix_my_data_stable import fix_my_data_stable
from utils.g_spread import save_log, load_cust_api

from datetime import datetime
from dotenv import load_dotenv
import toml, os, json
load_dotenv('.env')


def run() -> None:
    Total_cost = 0.0
    st.title("Test of Hypothesys Assistant")
    st.write("Please load here your data and ask me questions about it! ")
    try:
        user_email = st.experimental_user.email
        user = user_email.split('@')[0]
    except:
        user_email = 'dev'
        user = 'dev'

    if  user_email is not None:
        st.write(f"Greetings, {user_email} 👋")

    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read the Excel file into a DataFrame
#        try:
        data = pd.read_excel(uploaded_file)
        source_text = import_text_stat()

        user_query = st.chat_input("What do you want to test from this data?")
        if user_query:
            response, total_cost = recommend_test(source_text, data, user_query)
            Total_cost = Total_cost + float(total_cost)
            st.write(response)
            
            if response:
                test_name, dependent_variable, independent_variable = find_dep_ind_var(response)
                #debug script
                #st.write('The most appropriate test is: ',test_name)
                #for dv in dependent_variable:    st.write('Dependent variable(s)  : ',dv)
                #for iv in independent_variable:  st.write('Independent variable(s): ',iv)


                test_name_1, dependent_variable_, independent_variable_, hypothesis, total_cost = find_dep_ind_var_0(response)
                Total_cost = Total_cost + float(total_cost)

                
                with open('Tests/'+str(test_name), 'r') as file:
                    test_of_hypothesys_content = file.read()
                #debug script
                #st.write('hypothesis is: ',hypothesis)
                #st.write('Content is: ',test_of_hypothesys_content)
                data, total_cost = fix_my_data_stable(data,test_of_hypothesys_content, hypothesis)
                Total_cost = Total_cost + float(total_cost)
                
                st.write(data.columns)
                st.write(data[:5])

                test_of_h = None
                if test_name:
                    print('Running', test_name)
                    test_of_h = run_test(data,test_name,dependent_variable,independent_variable)

                if test_of_h  is not None:
                    # Assuming interpret_results is also defined
                    results_interpretation, total_cost = interpret_results(test_of_h , data)
                    Total_cost = Total_cost + float(total_cost)
                    st.write("Results Interpretation:")
                    st.write(results_interpretation)

                    current_datetime = datetime.now()
                    log_info = ['Stat_assistant_v1.py',
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
#        except:
#            st.write('It seems that something is wrong with your dataset. Please review it.\n')
#            st.write('You can ask for the help of our "Test of hypothesys advisor.\n')
#            st.markdown("[Advisor (select me from the dropdown list on the left)](https://way2stat.streamlit.app/#test-of-hypothesis-advisor)")
#            st.write('Remember to make sure to follow this template when uploading your data: \n')
#            st.markdown("[Template](https://docs.google.com/spreadsheets/d/11FLvCX_dw0jsNJG7wBGPLAleQBrZJHV4/edit?usp=sharing&ouid=100261840869406723359&rtpof=true&sd=true)")
    
    if __name__ == "__main__":
        run()