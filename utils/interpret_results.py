def interpret_results(answer, data, api_key):
    import os
    from openai import OpenAI
    from dotenv import load_dotenv
    import pandas as pd
    from utils.check_cost import check_cost
    load_dotenv('.env')

    #import excel file
    data_str=data[:10].to_string()

    #api_key = os.getenv('OPENAI_API_KEY')
    # Define the prompt you want to send to the API
    prompt=''' Please interpret the results that you will be provided with.
     these results come from a test of hypothesis based on this dataset: '''+str(data_str)+'''
     Please be very accurate and discoursive. Imagine to be a professor explain the results to a student.'''

    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": answer}
    ],
    temperature=0
    )
    total_cost = check_cost(response, model = "gpt-4o-mini")
    response=response.choices[0].message.content
    
    return response, total_cost
