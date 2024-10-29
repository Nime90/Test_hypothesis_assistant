def RepeatedMeasuresLogisticRegression(data,dep_var,ind_var):
    import statsmodels.formula.api as smf
    import pandas as pd
    import seaborn as sns
    import statsmodels.discrete.discrete_model as dm
    Col_end = dep_var
    Col_exo = ind_var

    model= smf.logit(formula=str(Col_end)+' ~ C('+str(Col_exo)+')', data= data).fit()
    results = model.summary()
    return results.to_string()
