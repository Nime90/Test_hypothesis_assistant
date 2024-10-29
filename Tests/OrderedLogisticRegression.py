#OrderedLogisticRegression
x=0
while x==0:
    try:
        import pandas as pd
        from statsmodels.miscmodels.ordinal_model import OrderedModel

        print('Ordered logistic regression is used when the dependent variable is ordered, but not continuous.\n')
        file_name=input('Please insert here the excel file name: ')
        d_var=input('Please insert here the dependent variable name: ')
        i_var=input('Please insert here the independent variable(s) name(s) comma separated (e.g. col1,col2,col3): ')
        ind_var=i_var.split(',')

        data=pd.read_excel(str(file_name)+'.xlsx')
        mod_prob = OrderedModel(data[str(d_var)], data[ind_var], distr='logit')

        print(' ')
        res_log = mod_prob.fit(method='bfgs')
        print(' ')

        print(res_log.summary())
        x=1
    except Exception as e: 
        print(e)
        x=0
input('Please press enter to kill me!')