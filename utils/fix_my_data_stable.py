def build_a_function(data,test_of_hypothesys, hypothesys):
    import os
    from openai import OpenAI
    from dotenv import load_dotenv
    import pandas as pd
    from utils.check_cost import check_cost
    load_dotenv('env')

    #import excel file
    data_str=data[:50].to_string()

    api_key = os.getenv('OPENAI_API_KEY')
    # Define the prompt you want to send to the API
    prompt=f''' 
            You will be provvided with a dataset and your only job is to build a python file that restructure the data in the dataset 
            to make them work in this test: {test_of_hypothesys}.
            The objective of this test is to fulfill this hypothesis:  {hypothesys}.
            Given thi hypothesis, please identify the dependent and independent variables in the provvided data.
            Make sure to name the columns with the same names of the independent and dependent variables in the fixed data.

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
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": data_str}
    ],
    temperature=0
    )
    total_cost = check_cost(response, model = "gpt-4o-mini")
    response=response.choices[0].message.content
    response=response.replace("```python",'').replace("```","")

    with open('utils/fix_my_data_temp.py', "w") as file:   file.write(response)
    print('utils/fix_my_data_temp.py creation is completed. it costed '+ str(total_cost)+'US dollars')
    return total_cost

def fix_my_data_stable(data,test_of_hypothesys, hypothesys):
    total_cost = build_a_function(data,test_of_hypothesys, hypothesys)
    from utils.fix_my_data_temp import fix_my_data_temp
    data_fixed = fix_my_data_temp(data)
    return data_fixed, total_cost