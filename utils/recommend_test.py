def recommend_test(source_text, data, message):
    import os, random , numpy as np
    from openai import OpenAI
    from dotenv import load_dotenv
    import pandas as pd
    from utils.check_cost import check_cost
    load_dotenv('env')

    #import excel file
    data_str=data[:40].to_string()
    all_files = os.listdir('Tests')
    all_tests=''
    for a in all_files:
        all_tests+=a+', '

    api_key = os.getenv('OPENAI_API_KEY')
    # Define the prompt you want to send to the API
    prompt=''' You are a professor and a student tried to formulate a test of hypothesis.
    Firstyly evaluate the test of hypothesis formulated and if needed reformulate a proper test of hypothesis.
    After that: You are only allowed to answer the questions about Test of hypotesis 
    based on the following information: ''' + source_text + '. Given this dataset: '+ data_str+''' 
    . After that select the recommended test from this list: '''+all_tests+'''. 
    Finally specify the test, the dependent varible and independent variable(s) in the end of the message.
    It is important to do not change the name of the test provvided in the list.
    Provide the answer as follows:\n 
    Test of hypothesys: [well formulated test of hypothesis]\n
    Explanation: [a quick but complete explanation of the selected test]\n
    Test: [name.py], Dependent Variable: [name], Independent Variable: [name].\n'''

    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": message}
    ],
    temperature=0 
    )
    total_cost = check_cost(response, model = "gpt-4o-mini")
    response=response.choices[0].message.content
    return response, total_cost

def recommend_test_nodata(source_text, message):
    import os, random , numpy as np
    from openai import OpenAI
    from dotenv import load_dotenv
    import pandas as pd
    from utils.check_cost import check_cost
    load_dotenv('env')

    #import excel file
    all_files = os.listdir('Tests')
    all_tests=''
    for a in all_files:
        all_tests+=a+', '

    api_key = os.getenv('OPENAI_API_KEY')
    # Define the prompt you want to send to the API
    prompt=''' You are a professor and a student tried to formulate a test of hypothesis.
    Firstyly evaluate the test of hypothesis formulated and if needed reformulate a proper test of hypothesis.
    After that: You are only allowed to answer the questions
    based only on the following information: ''' + source_text +''' 
    . After that select the recommended test from this list: '''+all_tests+'''. 
    Finally specify the test, the dependent varible(s) and independent variable(s) in the end of the message.
    Please provvide a complete and exaustive answer and some examples if possible, like a professor would do to students.
    It is very important that in your answer NEVER mention SPSS. Use the provided knowledge just to provide examples.'''

    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": message}
    ],
    temperature=0
    )

    total_cost = check_cost(response, model = "gpt-4o-mini")
    response=response.choices[0].message.content

    return response, total_cost
