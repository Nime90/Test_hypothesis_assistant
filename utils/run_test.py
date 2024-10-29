def run_test(data,test_name,dependent_variable,independent_variable):
    import streamlit as st
    from Tests.TwoIndependentSampleTtest import IndSamplesTtest
    from Tests.FactorialAnova import FactorialANOVA
    from Tests.AnalysisOfCovariance import AnalysisOfCovariance
    from Tests.ChiSquare import Chisquare
    from Tests.BinomialTest import BinomialTest
    from Tests.Correlation import correlation

    test_of_h = None
    if 'TwoIndependentSampleTtest.py' in str(test_name) and dependent_variable and independent_variable:
        test_of_h = IndSamplesTtest(data, column1=dependent_variable, column2=independent_variable[0], P_value=0.05, tails=2)
    elif 'FactorialAnova.py' in str(test_name) and dependent_variable and independent_variable:
        test_of_h = FactorialANOVA(data, dependent_variable, independent_variable)
    elif 'AnalysisOfCovariance.py' in str(test_name) and dependent_variable and independent_variable:
        test_of_h = AnalysisOfCovariance(data, dependent_variable, independent_variable)
    elif 'ChiSquare.py' in str(test_name) and dependent_variable and independent_variable:
        test_of_h = Chisquare(data, independent_variable[0], dependent_variable, P_value=0.05)
    elif 'BinomialTest.py' in str(test_name) and dependent_variable:
        test_of_h = BinomialTest(data, dependent_variable)
    elif 'Correlation.py' in str(test_name) and dependent_variable and independent_variable:
        test_of_h = correlation( data, dependent_variable, independent_variable[0] )
    
    return test_of_h