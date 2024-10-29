def OneWayRepeatedMeasuresANOVA(data,Col_dep_var,Col_subject,Col_repeated_measure,P_value=0.05):
    from statsmodels.stats.anova import AnovaRM

    message = AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit()
    #F=str(AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit()).split('\n')[4].split(' ')[1]
    #dof=str(AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit()).split('\n')[4].split(' ')[2]
    p=str(AnovaRM(data=data, depvar=str(Col_dep_var), subject=str(Col_subject), within=[str(Col_repeated_measure)]).fit()).split('\n')[4].split(' ')[4]
    
    if round(float(p),4) < round(float(P_value),4): message=+'\nOne-way repeated measures analysis of variance suggests that there is a statistically significant effect of '+str(Col_repeated_measure)+' at the '+str(P_value)+' level.'
    else: message=+'\nOne-way repeated measures analysis of variance suggests that THERE IS NOT a statistically significant effect of '+str(Col_repeated_measure)+' at the '+str(P_value)+' level.'
    return message
    
