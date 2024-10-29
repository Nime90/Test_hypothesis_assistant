#OneSample Median-test
def OneSampleMediantest(file_name,column,popmean,P_value):
    import pandas as pd 
    from scipy.stats import wilcoxon
    data=pd.read_excel(str(file_name)+'.xlsx')
    w, p = wilcoxon(data[str(column)])
    print('\nWe are now checking whether the median of column "'+str(column)+'" differs significantly from "'+str(popmean)+'"\n', '\nIn this case the t-statistic score is: '+str(w)+' and the p-value is: '+str(round(float(p),4))+'.\n')
    if round(float(p),4) < P_value:
        message='The median of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].median())+', which is statistically significantly different from the test value of "'+str(popmean)+'".\n'
    else:
        message='The median of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].median())+', which is NOT statistically significantly different from the test value of "'+str(popmean)+'".\n'
    return message
##### input data from here ####
x=0
while x==0:
    try:
        print('A one sample median test allows us to test whether a sample median differs significantly from a hypothesized value. We do not need to assume that it is interval and normally distributed (we only need to assume that the column is an ordinal variable).\n')
        file_name=input('Please insert here the excel file name: ')
        column=input('Please select the column you want to test: ')
        popmean=int(input ('Please insert here the hypothesized mean: '))
        P_value=float(input('Please insert here your P_value: '))
        try:
            result=OneSampleMediantest(file_name,column,popmean,P_value)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('\nPlease press enter to kill me!')