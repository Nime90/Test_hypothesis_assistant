#ChisquareGoodnessOfFit
def ChisquareGoodnessOfFit(data,column,exp_prop_0,P_value=0.05):
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    tails=1
    exp_prop=[]
    expected_data=[]

    exp_prop_0='0.1,0.1,0.1,0.7'
    observed_data=data[str(column)].value_counts().sort_index()
    o_dp='['
    for i in observed_data: o_dp=o_dp+str(round(i/sum(observed_data),2))+', '
    o_dp=o_dp+']'
    o_dp=o_dp.replace(', ]',']')
    o_d='['
    for o in observed_data:o_d=o_d+str(o)+', '
    o_d=o_d+']'
    o_d=o_d.replace(', ]',']')
    for i in exp_prop_0.split(','): exp_prop.append(float(i))
    for i in exp_prop: expected_data.append(int(len(data[str(column)])*float(i)))

    chi_square_test_statistic, p_value = stats.chisquare(observed_data, expected_data)
    message = '\nWe are now checking whether the observed proportions for '+str(column)+': '+str(o_dp)+' differ from hypothesized proportions: ['+str(exp_prop_0)+'].\n'+'The observed numbers are: '+str(o_d)+'\n'+'The expected numbers are: '+str(expected_data)
    message = message + '\nIn this case the  p-value is: '+str(round(float(p_value),3)*int(tails))+'.\n' + 'chi_square_test_statistic is : ' + str(round(chi_square_test_statistic,3))+'.\n' + 'Chi-square critical value is: '+str(round((stats.chi2.ppf(1-0.05, df=6)),3))
    if round(float(p_value),3)*int(tails) < P_value: 
        message = message + 'These results show that the composition in our sample for '+str(column)+' differ significantly from the hypothesized values that we supplied.\n'
    else: 
        message = message + '\nThese results show that the composition in our sample for '+str(column)+' DOES NOT differ significantly from the hypothesized values that we supplied.\n'
    return message
