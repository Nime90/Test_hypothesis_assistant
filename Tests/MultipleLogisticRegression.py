#MultipleLogisticRegression
def MultipleLogisticRegression(data,dep_var, ind_var):
        import pandas as pd
        import statsmodels.formula.api as smf
        cont_var=''
        indp_var=''
        for c in ind_var:
            if len(data[str(c)].unique()) > 7:
                cont_var =+ c+','
            else:
                indp_var =+ c+','

        #prep cont var
        cont_var=cont_var.replace(',','+')

        #prep cat var
        if len(indp_var)>2:
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

        result = model.summary()

        return result.to_string()