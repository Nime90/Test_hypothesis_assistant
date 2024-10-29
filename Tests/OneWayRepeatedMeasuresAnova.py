def OneWayRepeatedMeasuresANOVA(File_name,sheet_name,Col_dep_var,Col_subject,Col_repeated_measure,P_value):
    import numpy as np
    import pandas as pd
    from statsmodels.stats.anova import AnovaRM

    data=pd.read_excel(str(File_name)+'.xlsx',sheet_name=sheet_name)
    print('')
    print(AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit())
    #F=str(AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit()).split('\n')[4].split(' ')[1]
    #dof=str(AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit()).split('\n')[4].split(' ')[2]
    p=str(AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit()).split('\n')[4].split(' ')[4]
    
    if round(float(p),4) < round(float(P_value),4): message='\nOne-way repeated measures analysis of variance suggests that there is a statistically significant effect of '+str(Col_repeated_measure)+' at the '+str(P_value)+' level.'
    else: message='\nOne-way repeated measures analysis of variance suggests that THERE IS NOT a statistically significant effect of '+str(Col_repeated_measure)+' at the '+str(P_value)+' level.'
    return message
    
##### input data from here ####
x=0
while x==0:
    try:
        print('\nYou would perform a one-way repeated measures analysis of variance if you had one categorical independent variable and a normally distributed interval dependent variable that was repeated at least twice for each subject.  This is the equivalent of the paired samples t-test, but allows for two or more levels of the categorical variable. This tests whether the mean of the dependent variable differs by the categorical variable\n')
        File_name=input('Please insert here the excel file name: ')
        sheet_name=input('Please insert here the sheet name in the file: ')
        Col_dep_var=input('Please select the name of the dependent variable column: ')
        Col_subject=input('Please select the name of the subject variable column: ')
        Col_repeated_measure=input('Please select the name of the repeated measure variable column: ')
        P_value=float(input(' Please insert here your P_value: '))

        try:
            result=OneWayRepeatedMeasuresANOVA(File_name,sheet_name,Col_dep_var,Col_subject,Col_repeated_measure,P_value)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('\nPlease press enter to kill me!')