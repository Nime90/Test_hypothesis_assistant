#NOT WORKING: IT STOPS WHEN SELECTING THE TEST
import streamlit as st
import pandas as pd
from utils.import_text_stat import import_text_stat, import_text_stat_standard
from utils.recommend_test import recommend_test_nodata
from utils.interpret_results import interpret_results
from utils.run_test import run_test
from utils.find_dep_ind_var import find_dep_ind_var

st.title("Hypothesis Testing Assistant")

user_query = st.chat_input("What do you want to test from this data?")
if user_query is not None:
    #source_text = import_text_stat('https://stats.oarc.ucla.edu/spss/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-spss/')
    source_text = import_text_stat_standard()
    response = recommend_test_nodata(source_text, user_query)
    st.write(response)
