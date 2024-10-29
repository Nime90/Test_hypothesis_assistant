#Correlation
def correlation( data,dependent_variable, independent_variable ):
    from scipy.stats import pearsonr
    import pandas as pd
    print('A correlation is useful when you want to see the relationship between two (or more) normally distributed interval variables\n')

    col1=dependent_variable
    col2=independent_variable
    P_value=0.05


    corr, p = pearsonr(data[str(col1)], data[str(col2)])
    prop=(corr*corr)*100

    if round(p,4)<round(P_value,4): res='is'
    else: res='IS NOT'

    message='The Pearson correlation score between the two columns is '+str(round(corr,4))+'. Hence "'+str(col1)+'" shares about '+str(round(prop,2))+'%'+' of its variability with "'+str(col2)+'". '+'Since the p_value is '+str(round(p,4))+' this correlation '+str(res)+' statistically significant!'
    return message