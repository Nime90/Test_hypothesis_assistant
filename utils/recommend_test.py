def recommend_test(source_text, data, message):
    import os, random , numpy as np
    from openai import OpenAI
    from dotenv import load_dotenv
    import pandas as pd
    load_dotenv('env')

    # Set a fixed random seed
    random.seed(42)
    np.random.seed(42)
    #import excel file
    data_str=data[:10].to_string()
    all_files = os.listdir('Tests')
    all_tests=''
    for a in all_files:
        all_tests+=a+', '

    api_key = os.getenv('OPENAI_API_KEY')
    # Define the prompt you want to send to the API
    prompt=''' You are only allowed to answer the questions about Test of hypotesis 
    based on the following information: ''' + source_text + '. Given this dataset: '+ data_str+''' 
    . After that select the recommended test from this list: '''+all_tests+'''. 
    Finally specify the test, the dependent varible and independent variable(s) in the end of the message.
    It is important to do not change the name of the test provvided in the list.
    Provide the last as follows: Test: [name.py], Dependent Variable: [name], Independent Variable: [name]. '''

    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": message}
    ],
    temperature=0 
    )

    response=response.choices[0].message.content
    return response