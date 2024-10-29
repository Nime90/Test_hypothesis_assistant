#OneSample t-test
def OneSampleTtest(file_name,column,popmean,P_value):
    import pandas as pd 
    import scipy.stats as stats
    data=pd.read_excel(str(file_name)+'.xlsx')
    t_statistic, p_value = stats.ttest_1samp(a=data[str(column)], popmean=popmean)
    print('\nWe are now checking whether the average of column "'+str(column)+'" differs significantly from "'+str(popmean)+'"\n', '\nIn this case the t-statistic score is: '+str(t_statistic)+'and the p-value is: '+str(round(float(p_value),4))+'.\n')
    if round(float(p_value),4) < P_value:
        message='The mean of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].mean())+', which is statistically significantly different from the test value of "'+str(popmean)+'".\n'
    else:
        message='The mean of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].mean())+', which is NOT statistically significantly different from the test value of "'+str(popmean)+'".\n'
    return message
##### input data from here ####
x=0
while x==0:
    try:
        print('A one sample t-test allows us to test whether a sample mean (of a normally distributed interval variable) significantly differs from a hypothesized value.\n','\nPlease enter the following information to perform a One Sample T-test of the mean.\n')
        file_name=input('Please insert here the excel file name: ')
        column=input('Please select the column you want to test: ')
        popmean=int(input ('Please insert here the hypothesized mean: '))
        P_value=float(input('Please insert here your P_value: '))
        try:
            result=OneSampleTtest(file_name,column,popmean,P_value)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('\nPlease press enter to kill me!')