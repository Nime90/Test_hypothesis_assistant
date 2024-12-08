#Multivariate multiple regression
def MultivariateMultipleregression(data, dependent_variable, independent_variable):
    import numpy as np,pandas as pd
    from statsmodels.multivariate.manova import MANOVA

    dep_var=''
    for d in dependent_variable:
        dep_var = dep_var + str(d) + ','
    dep_var = dep_var[:-1]

    ind_var=''
    for id in independent_variable:
        dep_var = dep_var + str(id) + ','
    ind_var = ind_var[:-1]

    fit = MANOVA.from_formula(str(dep_var).replace(',','+')+' ~ '+str(ind_var).replace(',','+'), data=data)
    results = fit.mv_test()

    return results.to_string()