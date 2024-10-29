#FactorialANOVA
def FactorialANOVA(file_name,dep_var,ind_var,n,posthoc='N',ph_col=''):
    import numpy as np
    import pandas as pd
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    import scikit_posthocs as sp

    data=pd.read_excel(str(file_name)+'.xlsx')
    # Performing Factorial ANOVA
    model = ols(str(dep_var)+' ~ '+str(ind_var), data=data).fit()
    print(sm.stats.anova_lm(model, typ=n))
    
    if posthoc=='Y':
        print('')
        print('results for the posthoch test on the column "'+str(ph_col)+'": ')
        print('')           
        print(sp.posthoc_ttest(data, val_col=str(dep_var), group_col=str(ph_col), p_adjust='holm'))

##### input data from here ####
x=0
while x==0:
    try:
        print('\nA factorial ANOVA has two or more categorical independent variables (either with or without the interactions) and a single normally distributed interval dependent variable.\n')
        file_name=input('Please insert here the excel file name: ')
        dep_var=input('Please specify here the column with the dependent variable: ')
        ind_var=input('Please insert here 2 or more independent categorical variables conncted by the "+" sign and a capital "C()" in front of it. Eventually please indicate the interaction between the variables as per example (e.g. C(col1) + C(col2) + C(col1):C(col2): ')
        n=int(input('Please insert here the amount of independent categorical variables (i.e. if you are using 2 independent variables, please write 2: '))
        posthoc= input("Do you want to perform a posthoc test? please enter only 'Y' or 'N': " )
        if posthoc=='Y': ph_col= input("If yes, please enter the name of the column for the posthoc test: " )

        try:
            FactorialANOVA(file_name,dep_var,ind_var,n,posthoc,ph_col)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('\nPlease press enter to kill me!')