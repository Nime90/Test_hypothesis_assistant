#Chisquare
def Chisquare(data,ind_var,dep_var):
    import pandas as pd
    from scipy.stats import chi2_contingency

    col1 = ind_var
    col2 = dep_var
    contingency_table = pd.crosstab(data[col1], data[col2])
    chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)

    message=str("These are the results from the Chi-square test: \n"
                "1. chi2_stat: "+ str(chi2_stat)+"\n"+
                "2. p_value: "+ str(p_val)+"\n"+
                "3. dof: "+str(dof)+"\n"+
                "4. Contingency table: ["+str(contingency_table.to_string())+"]"+"\n"+
                "5. expected: "+ str(expected)
                )
    
    return message

