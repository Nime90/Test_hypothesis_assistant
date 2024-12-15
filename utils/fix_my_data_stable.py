def fix_my_data_stable(data,test_of_hypothesys, hypothesys):
    import os
    from openai import OpenAI
    from dotenv import load_dotenv
    import pandas as pd
    from utils.check_cost import check_cost
    load_dotenv('env')
    import streamlit as st

    #import excel file
    data_str=data[:50].to_string()

    api_key = os.getenv('OPENAI_API_KEY')
    # Define the prompt you want to send to the API
    prompt=f''' 
            You will be provvided with a dataset and your only job is to build a python file that 
            restructure the data in the dataset to make them work in this test: {test_of_hypothesys}.
            The objective of this test is to fulfill this hypothesis:  {hypothesys}.
            Given thi hypothesis, please identify the dependent and independent variables in the provvided data.
            Make sure to name the columns with the same names of the independent and dependent variables in the fixed data.
            Make sure that the function ALWAYS return a dataframe (pandas)
            Make sure that the fixed data has no Null values. Please clean it as good as you can.
            Please only return the function. No introduction or explanation is needed
            It is important that the output is always as follows:
            
            def fix_my_data_temp(data,dependent_variable_name=<insert the name of the dependent varaible you found>,independent_variable_name_1<insert the name of the independent varaible you found>,independent_variable_name_2...):
                #import all the needed libraries
                import pandas as pd

                #insert here all the needed steps to fix the data
                ...

                #make sure that the columns name are the same as the identified dependent and independent varaibles
                fixed_dataset.columns=[dependent_variable_name,independent_variable_name_1,...]
                return fixed_dataset
            '''
    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": data_str}
    ],
    temperature=0
    )
    total_cost = check_cost(response, model = "gpt-4o")
    response=response.choices[0].message.content
    response=response.replace("```python",'').replace("```","")

    with open('utils/fix_my_data_temp.py', "w") as file:   file.write(response)
    st.write('utils/fix_my_data_temp.py creation is completed. it costed '+ str(total_cost)+'US dollars')

    prompt_expl=f''' 
            You will be provvided with a dataset and your only job is to describe what you would change 
            in this data to make it work in this test: {test_of_hypothesys}.
            The objective of this test is to fulfill this hypothesis:  {hypothesys}.
            Please be precise, sinteitc and to the point without being too technical
            '''

    response_exp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt_expl},
        {"role": "user", "content": data_str}
    ],
    temperature=0
    )
    total_cost_exp = check_cost(response_exp, model = "gpt-4o-mini")
    total_cost = total_cost + float(total_cost_exp)
    response_exp=response_exp.choices[0].message.content
    st.write('resp_esxpl_debug',response_exp)
    return response_exp, total_cost