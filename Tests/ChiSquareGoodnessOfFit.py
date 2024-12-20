#ChisquareGoodnessOfFit
def ChisquareGoodnessOfFit(data, dependent_variable):
    import numpy as np
    from collections import Counter
    from scipy.stats import chi2

    #find the observed variables
    responses = [i for i in data[str(dependent_variable)]]
    # Define the categories
    categories = data[str(dependent_variable)].unique()
    # Compute the observed frequencies using Counter
    observed_counts = Counter(responses)
    # Ensure the observed frequencies are in the same order as the categories
    observed = [observed_counts[color] for color in categories]
    # Assume an equal distribution (uniform expectation)
    total_responses = len(responses)
    num_categories = len(categories)
    expected = [total_responses / num_categories] * num_categories
    
    # Ensure the inputs are numpy arrays
    observed = np.array(observed)
    expected = np.array(expected)

    # Check if lengths match
    if len(observed) != len(expected):
        raise ValueError("Observed and expected frequencies must be the same length")

    # Compute the chi-square statistic
    chi2_stat = np.sum((observed - expected) ** 2 / expected)

    # Degrees of freedom: number of categories - 1
    dof = len(observed) - 1

    # Compute the p-value
    p_value = 1 - chi2.cdf(chi2_stat, dof)

    message = str('These are the results for the chisquared goodness of fit:\n',
                  'Chi-square Statistic: '+str(chi2_stat)+'\n',
                  'Chi-square p_value: '+str(p_value)+'\n', 
                  'Degree of freedom:'+str(dof)
                )
    return message

