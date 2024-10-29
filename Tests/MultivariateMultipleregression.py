#Multivariate multiple regression
def MultivariateMultipleregression(data, dep_var, ind_var):
    import numpy as np,pandas as pd
    from statsmodels.multivariate.manova import MANOVA

    fit = MANOVA.from_formula(str(dep_var).replace(',','+')+' ~ '+str(ind_var).replace(',','+'), data=data)
    results = fit.mv_test()

    return results.to_string()