#analysisofCovariance
def AnalysisOfCovariance(data, dep_var, ind_var):
    from pingouin import ancova
    import pandas as pd, warnings
    warnings.simplefilter("ignore")
    print('\nAnalysis of covariance is like ANOVA, except in addition to the categorical predictors you also have continuous predictors as well.\n')
    for c in ind_var:
        if len(data[str(c)].unique()) > 7:
            cont_var=c
        else:
            cat_var=c
            
    res=ancova(data=data, dv=str(dep_var), covar=str(cont_var), between=str(cat_var))

    return res.to_string()