def SimpleRegression(data, dep_var, indep_var):
    import statsmodels.api as sm
    col1=dep_var
    col2=indep_var

    #define response variable
    x = data[str(col2)]
    y = data[str(col1)]
    #add constant to predictor variables
    x = sm.add_constant(x)

    #fit linear regression model
    model = sm.OLS(y, x).fit()

    #view model summary
    result = model.summary()

    return result.to_string()
