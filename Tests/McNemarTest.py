#McNemarTest
def McNemarTest(data,column1,column2,P_value):
    from statsmodels.stats.contingency_tables import mcnemar
    import pandas as pd

    Groups=pd.crosstab(data[str(column1)], data[str(column2)])
    group1=[Groups[0][0],Groups[0][1]]
    group2=[Groups[1][0],Groups[1][1]]
    groups=[group1,group2]

    #Mcnemar Test
    p=round(float(str(mcnemar(groups, exact=False)).split('\n')[0].split(' ')[-1]),3)
    s=round(float(str(mcnemar(groups, exact=False)).split('\n')[1].split(' ')[-1]),3)
    message='\nThe P_value is: '+str(p)+' and the statistic is: '+str(s)+'.\n'
    if p<P_value: message=+'\nMcNemar’s chi-square statistic suggests that there a statistically significant difference in the proportion of "'+str(column1)+'" group and the proportion of "'+str(column2)+'" group.'
    else: message=+'\nMcNemar’s chi-square statistic suggests that THERE IS NOT a statistically significant difference in the proportion of "'+str(column1)+'" group and the proportion of "'+str(column2)+'" group.'
    return message