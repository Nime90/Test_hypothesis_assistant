#NOT WORKING: IT STOPS WHEN SELECTING THE TEST
import streamlit as st
import pandas as pd
from utils.import_text_stat import all_stat_page#, import_text_stat_standard
from utils.recommend_test import recommend_test_nodata


st.title("Hypothesis Testing Assistant")

user_query = st.chat_input("Ask me questions about test of hypothesis")
if user_query is not None:
    #source_text = import_text_stat('https://stats.oarc.ucla.edu/spss/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-spss/')
    source_text = all_stat_page()
    response = recommend_test_nodata(source_text, user_query)
    st.write(response)
