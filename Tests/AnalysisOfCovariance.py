#analysisofCovariance
def AnalysisOfCovariance(data, dep_var, ind_var):

    import pandas as pd
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    """
    Perform Analysis of Covariance (ANCOVA).

    Parameters:
        data (pd.DataFrame): DataFrame containing the data.
        dependent_var (str): The name of the dependent variable.
        ind_var (list): A list of independent variables (categorical groups and covariates).

    Returns:
        result (statsmodels.anova.AnovaResults): The result of the ANCOVA.
    """

    # Ensure all categorical variables are correctly typed
    for var in ind_var:
        if data[var].dtype == 'object':
            data[var] = data[var].astype('category')

    # Create the formula string for the model
    formula = f"{dep_var} ~ " + " + ".join(ind_var)
    
    # Fit the model
    model = ols(formula, data=data).fit()
    
    # Perform ANCOVA
    ancova_table = sm.stats.anova_lm(model, typ=2)  # Type 2 ANOVA table
    
    message = 'Tese is the results of the Ancova analysis:\n'+ str(ancova_table.to_string())
    
    return message

