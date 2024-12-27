def run():
    import streamlit as st
    user_info = st.experimental_user
    st.write("User Info:", user_info)


    import json, os, pandas as pd
    from dotenv import load_dotenv
    load_dotenv('.env')
    # Parse the JSON string into a dictionary
    credentials_json_str = str(os.getenv('credentials_json')).strip().replace('\n','\\n')
    st.write(credentials_json_str )
    credentials_dict = json.loads(credentials_json_str)
    st.write(credentials_dict)

if __name__ == "__main__":
    run()
