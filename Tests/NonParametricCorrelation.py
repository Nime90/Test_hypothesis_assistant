#NonParametricCorrelation
def NonParametricCorrelation(data, dep_var, indep_var ):
    from scipy import stats

    col1 = dep_var
    col2 = indep_var
    P_value = 0.05

    corr, p = stats.spearmanr(data[str(col1)], data[str(col2)])

    if round(p,4)<round(P_value,4): res='is'
    else: res='IS NOT'

    message = 'The Spearmanr correlation score between the two columns is '+str(round(corr,4))+'. '
    message = message+' Since the p_value is '+str(round(p,4))+' this correlation '+str(res)+' statistically significant!'
    return message