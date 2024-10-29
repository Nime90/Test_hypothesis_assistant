#ChisquareGoodnessOfFit
def ChisquareGoodnessOfFit(file_name,column,P_value,exp_prop_0):
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    tails=1
    exp_prop=[]
    expected_data=[]

    data=pd.read_excel(str(file_name)+'.xlsx')
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
    print('\nWe are now checking whether the observed proportions for '+str(column)+': '+str(o_dp)+' differ from hypothesized proportions: ['+str(exp_prop_0)+'].\n','The observed numbers are: '+str(o_d)+'\n','The expected numbers are: '+str(expected_data))
    print('\nIn this case the  p-value is: '+str(round(float(p_value),3)*int(tails))+'.\n', 'chi_square_test_statistic is : ' + str(round(chi_square_test_statistic,3))+'.\n', 'Chi-square critical value is: '+str(round((stats.chi2.ppf(1-0.05, df=6)),3)))
    if round(float(p_value),3)*int(tails) < P_value: message='These results show that the composition in our sample for '+str(column)+' differ significantly from the hypothesized values that we supplied.\n'
    else: message= '\nThese results show that the composition in our sample for '+str(column)+' DOES NOT differ significantly from the hypothesized values that we supplied.\n'
    return message

##### input data from here ####
x=0
while x==0:
    try:
        print('A chi-square goodness of fit test allows us to test whether the observed proportions for a categorical variable differ from hypothesized proportions.\n')
        file_name=input('Please insert here the excel file name: ')
        column=input('Please select the column you want to test: ')
        exp_prop_0=input('Please insert the expected proportion of the categorical varible including decimal, comma seprated without space (e.g. 0.1,0.1,0.1,0.7): ')
        P_value=float(input('Please insert here your P_value: '))
        try:
            result=ChisquareGoodnessOfFit(file_name,column,P_value,exp_prop_0)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('Please press enter to kill me!')