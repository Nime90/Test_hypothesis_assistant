#FactorialANOVA
def FactorialANOVA(data,dep_var,ind_var):
    import numpy as np
    import pandas as pd
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    import scikit_posthocs as sp
    from itertools import combinations

    def create_formula(ind_var):
        # Main terms
        main_terms = [f"C({var})" for var in ind_var]
        
        # Interaction terms
        interaction_terms = [
            ':'.join([f"C({var})" for var in combo]) 
            for r in range(2, len(ind_var) + 1) 
            for combo in combinations(ind_var, r)
        ]
        
        # Combine main and interaction terms
        formula = ' + '.join(main_terms + interaction_terms)
        return formula

    ind_var_txt=create_formula(ind_var)
    
    # Performing Factorial ANOVA
    model = ols(str(dep_var)+' ~ '+str(ind_var_txt), data=data).fit()
    n=len(ind_var)
    results=sm.stats.anova_lm(model, typ=n)
    
    for p in ind_var:
        post_hoc_res=sp.posthoc_ttest(data, val_col=str(dep_var), group_col=str(p), p_adjust='holm')
        post_hoc_res_txt='results for the posthoch test on the column "'+str(p)+'": '+post_hoc_res.to_string()

    return results.to_string() + '. '+str(post_hoc_res_txt)