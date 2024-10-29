#PairedSamplesTtest
def WilcoxonSignedRankSumTest(file_name,column1,column2,P_value=0.05,tails=2):
    import pandas as pd , numpy as np, scipy.stats as stats
    from statsmodels.stats.weightstats import ttest_ind

    data=pd.read_excel(str(file_name)+'.xlsx')
    group1=data[str(column1)]
    group2=data[str(column2)]

    t_statistic, p_value = stats.wilcoxon(group1, group2)
    if tails==1: p_value=p_value/2
    message='\nWe are now checking whether the average of column "'+str(column1)+'" differs significantly from the average in "'+str(column2)+'"\n' + '\nIn this case the t-statistic score is: '+str(round(float(t_statistic),4))+' and the p-value is: '+str(round(float(p_value),4))
    if round(float(p_value),4) < P_value:
        message=+'\nThe mean of the variable "'+str(column1)+'" is '+str(round(group1.mean(),2))+', which is statistically significantly different from the mean of  "'+str(column2)+'": '+str(round(group2.mean(),2))+' for a P-Value<'+str(P_value)+'.\n'
    else:
        message=+'\nThe mean of the variable "'+str(column1)+'" is '+str(round(group1.mean(),2))+', which IS NOT statistically significantly different from the mean of  "'+str(column2)+'": '+str(round(group2.mean(),2))+' for a P-Value<'+str(P_value)+'.\n'

    return message
