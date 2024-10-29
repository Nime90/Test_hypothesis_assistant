#McNemarTest
def McNemarTest(file_name,column1,column2,P_value):
    from statsmodels.stats.contingency_tables import mcnemar
    import pandas as pd
    data=pd.read_excel(str(file_name)+'.xlsx')
    Groups=pd.crosstab(data[str(column1)], data[str(column2)])
    group1=[Groups[0][0],Groups[0][1]]
    group2=[Groups[1][0],Groups[1][1]]
    groups=[group1,group2]

    #Mcnemar Test
    p=round(float(str(mcnemar(groups, exact=False)).split('\n')[0].split(' ')[-1]),3)
    s=round(float(str(mcnemar(groups, exact=False)).split('\n')[1].split(' ')[-1]),3)
    print('\nThe P_value is: '+str(p)+' and the statistic is: '+str(s)+'.\n')
    if p<P_value: message='\nMcNemar’s chi-square statistic suggests that there a statistically significant difference in the proportion of "'+str(column1)+'" group and the proportion of "'+str(column2)+'" group.'
    else: message='\nMcNemar’s chi-square statistic suggests that THERE IS NOT a statistically significant difference in the proportion of "'+str(column1)+'" group and the proportion of "'+str(column2)+'" group.'
    return message

##### input data from here ####
x=0
while x==0:
    try:
        print('\nYou would perform McNemar’s test if you were interested in the marginal frequencies of two binary outcomes. These binary outcomes may be the same outcome variable on matched pairs (like a case-control study) or two outcome variables from a single group.')
        file_name=input('\nPlease insert here the excel file name: ')
        column1=input('Please select the first normally distributed interval dependent column you want to test: ')
        column2=input('Please select the second normally distributed interval dependent column you want to test: ')
        P_value=float(input('Please insert here your P_value: '))
        try:
            result=McNemarTest(file_name,column1,column2,P_value)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('Please press enter to kill me!')