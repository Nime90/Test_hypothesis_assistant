#FactorialLogisticRegression
def FactorialLogisticRegression(data, dep_var, ind_var):
        print('A factorial logistic regression is used when you have two or more categorical independent variables but a dichotomous dependent variable.\n')
        import pandas as pd
        import statsmodels.formula.api as smf

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

        result = model.summary()
        return result