def save_log(log_info, credentials_json_str):
    import gspread
    import json
    # Parse the JSON string into a dictionary
    credentials_dict = json.loads(credentials_json_str)
    
    # Use the dictionary to authenticate
    gc = gspread.service_account_from_dict(credentials_dict)

    # Access a public Google Sheet by its URL
    sheet_url = "https://docs.google.com/spreadsheets/d/18aGkib26C8U7tiFZ86rMru9ZT65GaaNr0m9cIt3nk9Y/edit#gid=0"
    
    # Open the sheet by URL
    sheet = gc.open_by_url(sheet_url).sheet1

    # Append the log info
    sheet.append_row(log_info)
    
    print('log correctly saved')

def load_cust_api(user_email):
    import gspread
    import json, os, pandas as pd
    from dotenv import load_dotenv
    load_dotenv('.env')
    # Parse the JSON string into a dictionary
    credentials_json_str = str(os.getenv('credentials_json'))
    credentials_dict = json.loads(credentials_json_str)

    # Use the dictionary to authenticate
    gc = gspread.service_account_from_dict(credentials_dict)

    # Access a public Google Sheet by its URL
    sheet_url = "https://docs.google.com/spreadsheets/d/1KFeFzqN9TRQfWvCh4xTF6WakMAIAzDdY2oSx3hTSwLA/edit#gid=0"

    # Open the sheet by URL
    sheet = gc.open_by_url(sheet_url).sheet1

    # Get all records as a list of dictionaries
    data = sheet.get_all_records()

    # Convert to a DataFrame
    df = pd.DataFrame(data)
    df1 = df[df['user_email']==str(user_email)]
    df1.reset_index(inplace=True)
    api_key = df1.api_key[0]
    return api_key

