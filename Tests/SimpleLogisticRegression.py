#SimpleLogisticRegression
def SimpleLogisticRegression(data,dep_var, ind_var):
    import pandas as pd
    import statsmodels.formula.api as smf

    model=smf.logit(str(dep_var)+" ~ "+str(ind_var), data = data).fit()
    results = model.summary()

    return results.to_string()