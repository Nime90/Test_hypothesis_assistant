def find_dep_ind_var(response):
    import re
    # Patterns for extracting relevant values
    test_pattern = r"Test:\s*([^,]+)"
    dependent_var_pattern = r"Dependent Var\s*(.*)"
    independent_var_pattern = r"Independent Var\s*(.*)"
    subject_column_pattern = r"Subject Column Name*(.*)"


    # Extract using regular expressions with case insensitivity
    response_final=response[response.find('Test:'):]
    test = re.search(test_pattern, response_final, re.IGNORECASE)
    dependent_var = re.search(dependent_var_pattern, response_final, re.IGNORECASE)
    independent_var = re.search(independent_var_pattern, response_final, re.IGNORECASE)
    subject_var = re.search(subject_column_pattern, response_final, re.IGNORECASE)

    # Store values in variables if they are found
    test_name = test.group(1).strip() if test else None
    dependent_variable   =   dependent_var.group(1).strip().split(':')[1].strip().replace(',','').replace('.','').split(' ') if dependent_var else None
    independent_variable = independent_var.group(1).strip().split(':')[1].strip().replace(',','').replace('.','').split(' ') if independent_var else None
    subject_var = subject_var.group(1).strip().split(':')[1].strip().replace(',','').replace('.','').split(' ') if subject_var  else None
    return test_name, dependent_variable, independent_variable, subject_var

def find_dep_ind_var_0(text, api_key):
    import os, json
    from openai import OpenAI
    from dotenv import load_dotenv
    import pandas as pd
    from utils.check_cost import check_cost
    load_dotenv('.env')

    # Define the prompt you want to send to the API
    prompt=''' 
    Given the provvided text, please identify:
     1. test_name, 
     2. dependent_variable, 
     3. independent_variable, 
     4. hypothesis
    
    It is important that the output needs to be in this format:
    {"test_name": "<insert here test name>", 
      "dependent_variable": "<[insert here dependent_variable(s)]>", 
      "independent_variable": "<[insert here independent_variable(s)]>", 
      "hypothesis": "<insert here the hypothesis>", 
      }

      Please do not add any intro nor explanation to the resutls.
            '''

    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
    ],
    temperature=0
    )
    total_cost = check_cost(response, model = "gpt-4o-mini")

    response=response.choices[0].message.content
    response=response.replace("```python",'').replace("```","")

    response_dic = json.loads(response)
    test_name = response_dic['test_name']
    dependent_variable=response_dic['dependent_variable']
    independent_variable = response_dic['independent_variable']
    hypothesis = response_dic['hypothesis']

    print(total_cost, test_name, dependent_variable, independent_variable, hypothesis)

    return test_name, dependent_variable, independent_variable, hypothesis, total_cost
