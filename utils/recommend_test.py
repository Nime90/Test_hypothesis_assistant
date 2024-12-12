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
    Explanation: [Please explain what is the selected test and why it is the most appropriate]\n
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
    import pandas as pd, json
    from utils.check_cost import check_cost
    load_dotenv('env')

    #import excel file
    all_files = os.listdir('Tests')
    all_tests=''
    for a in all_files:
        all_tests+=a+', '

    api_key = os.getenv('OPENAI_API_KEY')
    # Define the prompt you want to send to the API
    prompt=''' You are a professor and a student has a question on a test of hypothesis.
    Firstyly evaluate the test of hypothesis formulated (if any) and if needed, reformulate a proper test of hypothesis.
    After that: You are only allowed to answer the questions
    based only on the following information: ''' + source_text +''' . 
    After that select the most appropriate test from this list: '''+all_tests+'''. 
    Finally provvide a realistic example of how to use and interpret the selected test.
    Please provvide a complete and exaustive answer like a professor would do to students.
    It is very important that in your answer NEVER mention SPSS. Use the provided knowledge just to provide examples.
    Please always return the output in this format:
    "{"response: "< insert here the generated response >"
      "Selected Hypothesys": "<insert here the selected test of hypothesys as reported in the list (e.g. "ChiSquare.py")>"
    }'''

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
    response_dic= json.loads(response)
    with open('Tests/'+response_dic['Selected Hypothesys'], 'r') as file:
        test_content = file.read()
    
    prompt_tab = ''' Given the provided function, please return arealistic example of an ideal data structure in a small tabular form. 
    Please do not provvide an example of usage.'''
    recommended_data_structure = client.chat.completions.create(
    model="gpt-4o-mini", messages=[
        {"role": "system", "content": prompt_tab},
        {"role": "user", "content": test_content}
    ],
    temperature=0
    )
    total_cost = total_cost + float(check_cost(recommended_data_structure, model = "gpt-4o-mini"))
    recommended_data_structure_resp=recommended_data_structure.choices[0].message.content

    full_response = response_dic['response']+'\n \n'+recommended_data_structure_resp
    return full_response, total_cost
