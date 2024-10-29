def RepeatedMeasuresLogisticRegression(file_name,sheet_name,Col_end,Col_exo):
    import statsmodels.formula.api as smf
    import pandas as pd
    import seaborn as sns
    import statsmodels.discrete.discrete_model as dm

    data=pd.read_excel(str(file_name)+'.xlsx',sheet_name=sheet_name)
    model= smf.logit(formula=str(Col_end)+' ~ C('+str(Col_exo)+')', data= data).fit()
    return model.summary()
##### input data from here ####
x=0
while x==0:
    try:
        print('\nIf you have a binary outcome measured repeatedly for each subject and you wish to run a logistic regression that accounts for the effect of multiple measures from single subjects, you can perform a repeated measures logistic regression.\n')
        file_name=input('Please insert here the excel file name: ')
        sheet_name=input('Please insert here the sheet name in the file: ')
        Col_end=input('Please select the name of the dependent variable column: ')
        Col_exo=input('Please select the name of the independent (biary) variable column: ')

        try:
            result=RepeatedMeasuresLogisticRegression(file_name,sheet_name,Col_end,Col_exo)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('\nPlease press enter to kill me!')