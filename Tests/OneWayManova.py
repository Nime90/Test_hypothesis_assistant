#OneVayManova
def OneWayManova(data, dep_var, ind_var):
    from statsmodels.multivariate.manova import MANOVA
    dep_vars=''
    for d in dep_var: dep_vars=+ d+'+'
    fit = MANOVA.from_formula(str(dep_vars)[:-2]+' ~ '+str(ind_var), data=data)
    results = fit.mv_test()

    return results.to_string()