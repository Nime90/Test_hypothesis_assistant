import numpy as np
import statsmodels.api as sm
import pandas as pd
x=0
while x==0:
    try:
        print('\nSimple linear regression allows us to look at the linear relationship between one normally distributed interval predictor and one normally distributed interval outcome variable.\n')
        file_name=input('Please insert here the excel file name: ')
        col1=input('Please insert the name of the dependent variable: ')
        col2=input('Please insert the name of the independent variable: ')

        data=pd.read_excel(str(file_name)+'.xlsx')

        #define response variable
        x = data[str(col2)]
        y = data[str(col1)]
        
        #plot Current Situation
        import matplotlib.pyplot as plt
        plt.scatter(y,x, s = 10)
        plt.title('Scatter plot between: '+str(col1)+' and '+str(col2))
        #plt.show()

        #add constant to predictor variables
        x = sm.add_constant(x)

        #fit linear regression model
        model = sm.OLS(y, x).fit()

        #view model summary
        print(' ')
        print(model.summary())
        print('Printing the Graph')
        plt.show()
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')