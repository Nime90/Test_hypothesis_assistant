#FactorialLogisticRegression
x=0
while x==0:
    try:
        print('A factorial logistic regression is used when you have two or more categorical independent variables but a dichotomous dependent variable.\n')
        import pandas as pd
        import statsmodels.formula.api as smf
        file_name=input('Please insert here the excel file name: ')
        dep_var=input('Please insert here the name of the dichotomous dependent variable: ')
        indp_var=input('Please insert here the name of the categorical independent variables comma separated and NO SPACE (e.g. col1,col2,col3): ')
        ind_var=indp_var.split(',')

        data=pd.read_excel(str(file_name)+'.xlsx')

        for i in ind_var:
            cat_list =pd.get_dummies(data[str(i)], prefix=str(i))
            data=data.join(cat_list)

        ColToKeep=[]
        for c in data.columns:
            for i in ind_var:
                if str(i) in str(c): ColToKeep.append(c)

        formula=''
        for c in ColToKeep[2:]:
            if '_1' not in str (c): formula=formula+'C('+str(c)+')+'
        formula[:-1]

        model=smf.logit(str(dep_var)+" ~ "+str(formula[:-1]), data = data).fit()
        print(' ')
        print(model.summary())
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')