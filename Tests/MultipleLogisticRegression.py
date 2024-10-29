#MultipleLogisticRegression
x=0
while x==0:
    try:
        print('Multiple logistic regression is like simple logistic regression, except that there are two or more predictors.  The predictors can be interval variables or dummy variables, but cannot be categorical variables.  If you have categorical predictors, they should be coded into one or more dummy variables.\n')
        import pandas as pd
        import statsmodels.formula.api as smf
        file_name=input('Please insert here the excel file name: ')
        dep_var=input('Please insert here the name of the binary dependent variable: ')
        cont_var=input('Please insert here the name of the independent continuous variables comma separated (e.g. col1,col2,col3) - Leave it empty if not relevant: ')
        indp_var=input('Please insert here the name of the independent categorical variables comma separated (e.g. col1,col2,col3) - Leave it empty if not relevant: ')
        
        data=pd.read_excel(str(file_name)+'.xlsx')
        

        #prep cont var
        cont_var=cont_var.replace(',','+')

        #prep cat var
        if len(indp_var)>3:
            ind_var=indp_var.split(',')
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
        
            if len(cont_var)>2: formula=' + '+formula[:-1]
            else: formula=formula[:-1]
        else: formula=''
        model=smf.logit(str(dep_var)+" ~ "+str(cont_var)+str(formula), data = data).fit()
        print(' ')
        print(model.summary())
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')