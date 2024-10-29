#MultipleRegression
import numpy as np
import statsmodels.api as sm
import pandas as pd
x=0
while x==0:
    try:
        print('\nMultiple regression is very similar to simple regression, except that in multiple regression you have more than one predictor variable in the equation. \n')
        file_name=input('Please insert here the excel file name: ')
        col1=input('Please insert the name of the dependent variable: ')
        col2=input('Please insert the name of the independent variables comma separated (e.g. col1,col2,col3): ')
        ind_var=col2.split(',')
        data=pd.read_excel(str(file_name)+'.xlsx')

        #define response variable
        y = data[str(col1)]
        x = data[ind_var]

        #add constant to predictor variables
        x = sm.add_constant(x)

        #fit linear regression model
        model = sm.OLS(y, x).fit()

        #view model summary
        print(' ')
        print(model.summary())
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')