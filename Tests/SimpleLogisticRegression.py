#SimpleLogisticRegression
x=0
while x==0:
    try:
        print('\nLogistic regression assumes that the outcome variable is binary (i.e., coded as 0 and 1). \n')
        import pandas as pd
        import statsmodels.formula.api as smf
        file_name=input('Please insert here the excel file name: ')
        dep_var=input('Please insert here the name of the binary dependent variable: ')
        ind_var=input('Please insert here the name of the independent variable : ')


        data=pd.read_excel(str(file_name)+'.xlsx')

        model=smf.logit(str(dep_var)+" ~ "+str(ind_var), data = data).fit()
        print(' ')
        print(model.summary())
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')