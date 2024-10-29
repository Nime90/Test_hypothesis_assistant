#Multivariate multiple regression
x=0
while x==0:
    try:
        print('\nMultivariate multiple regression is used when you have two or more dependent variables that are to be predicted from two or more independent variables.\n')
        import numpy as np,pandas as pd
        from statsmodels.multivariate.manova import MANOVA
        file_name=input('Please insert here the excel file name: ')
        dep_var=input('Please enter here the names of the continuous dependent variables comma separated (e.g. col1,col2,col3): ')
        ind_var=input('Please enter here the name of the categorical independent variables comma separated (e.g. col1,col2,col3): ')
        data=pd.read_excel(str(file_name)+'.xlsx')

        fit = MANOVA.from_formula(str(dep_var).replace(',','+')+' ~ '+str(ind_var).replace(',','+'), data=data)
        print(fit.mv_test())
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')