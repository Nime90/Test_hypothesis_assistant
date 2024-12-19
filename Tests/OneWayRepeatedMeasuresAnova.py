def OneWayRepeatedMeasuresANOVA(data, subject_col,independent_variable, dependent_variable):
    from statsmodels.stats.anova import AnovaRM
    
    score_col = dependent_variable
    condition_col = independent_variable
    # Perform ANOVA
    anova = AnovaRM(data, depvar=score_col, subject=subject_col, within=[condition_col])
    anova_results = anova.fit()
    results = anova_results.summary()
    message="These are the results from the one-way repeated measures ANOVA test: \n"+str(results)
    return message
