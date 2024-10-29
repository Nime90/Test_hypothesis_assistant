#PairedSamplesTtest
def PairedSamplesTtest(file_name,column1,column2,P_value,tails):
    import pandas as pd , numpy as np, scipy.stats as stats
    from statsmodels.stats.weightstats import ttest_ind

    data=pd.read_excel(str(file_name)+'.xlsx')
    group1=data[str(column1)]
    group2=data[str(column2)]

    t_statistic, p_value = stats.ttest_rel(group1, group2)
    if tails==1: p_value=p_value/2
    print('\nWe are now checking whether the average of column "'+str(column1)+'" differs significantly from the average in "'+str(column2)+'"\n', '\nIn this case the t-statistic score is: '+str(round(float(t_statistic),4))+' and the p-value is: '+str(round(float(p_value),4)))
    if round(float(p_value),4) < P_value:
        message='\nThe mean of the variable "'+str(column1)+'" is '+str(round(group1.mean(),2))+', which is statistically significantly different from the mean of  "'+str(column2)+'": '+str(round(group2.mean(),2))+' for a P-Value<'+str(P_value)+'.\n'
    else:
        message='\nThe mean of the variable "'+str(column1)+'" is '+str(round(group1.mean(),2))+', which IS NOT statistically significantly different from the mean of  "'+str(column2)+'": '+str(round(group2.mean(),2))+' for a P-Value<'+str(P_value)+'.\n'

    return message
##### input data from here ####
x=0
while x==0:
    try:
        print('A paired (samples) t-test is used when you have two related observations (i.e., two observations per subject) and you want to see if the means on these two normally distributed interval variables differ from one another.\n')
        file_name=input('Please insert here the excel file name: ')
        column1=input('Please select the first normally distributed interval dependent column you want to test: ')
        column2=input('Please select the second normally distributed interval dependent column you want to test: ')
        P_value=float(input(' Please insert here your P_value: '))
        tails=input('Please specify the number of tails to use in the analysis (select between 1 or 2): ')
        try:
            result=PairedSamplesTtest(file_name,column1,column2,P_value,tails)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('\nPlease press enter to kill me!')