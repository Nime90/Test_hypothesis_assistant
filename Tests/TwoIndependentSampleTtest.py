#TwoIndependentSamplesTtest
def IndSamplesTtest(data, column1, column2, P_value, tails):
    import pandas as pd , numpy as np, scipy.stats as stats
    import streamlit as st
    from statsmodels.stats.weightstats import ttest_ind

    group1=data[str(column1)][data[str(column2)] > 0].reset_index(drop=True)
    group2=data[str(column1)][data[str(column2)] == 0].reset_index(drop=True)
    
    #Check variance
    if np.var(group1)>np.var(group2):
        if (round(np.var(group1)/np.var(group2))) < 4: eq_var=True
        else: eq_var=False
    else:
        if (round(np.var(group2)/np.var(group1))) < 4: eq_var=True
        else: eq_var=False

    t_statistic, p_value = stats.ttest_ind(a=group1, b=group2, equal_var=eq_var)
    if tails==1: p_value=p_value/2
    explanation='\nAn independent samples t-test is used when you want to compare the means of a normally distributed interval dependent variable for two independent groups.\n'+'\nWe are now checking whether the average of column "'+str(column1)+'" differs significantly between the gorups in column "'+str(column2)+'"\n', '\nIn this case the t-statistic score is: '+str(round(t_statistic,3))+' and the p-value is: '+str(round(float(p_value),4))
    if round(float(p_value),4) < P_value:
        message=str(explanation)+'\nThe mean of the variable "'+str(column1)+'" for group 1 (i.e. when "'+str(column2)+'" is equal to 1) is '+str(round(group1.mean(),2))+', which is statistically significantly different from the mean of group 2 (i.e. when "'+str(column2)+'" is equal to 0): '+str(round(group2.mean(),2))+' for a P-Value<'+str(P_value)+'.\n'
    else:
        message=str(explanation)+'\nThe mean of the variable "'+str(column1)+'" for group 1 (i.e. when "'+str(column2)+'" is equal to 1) is '+str(round(group1.mean(),2))+', which IS NOT statistically significantly different from the mean of group 2 (i.e. when "'+str(column2)+'" is equal to 0): '+str(round(group2.mean(),2))+' for a P-Value<'+str(P_value)+'.\n'
    return message