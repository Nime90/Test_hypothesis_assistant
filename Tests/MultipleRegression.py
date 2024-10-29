#MultipleRegression
def MultipleRegression(data, dep_var, ind_var):
    import statsmodels.api as sm

    #define response variable
    y = data[str(dep_var)]
    x = data[ind_var]

    #add constant to predictor variables
    x = sm.add_constant(x)

    #fit linear regression model
    model = sm.OLS(y, x).fit()

    #view model summary
    results=model.summary()
    return results.to_string()
