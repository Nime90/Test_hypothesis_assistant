#OneSample t-test
def OneSampleTtest(data,column,popmean,P_value=0.05):
    import scipy.stats as stats

    t_statistic, p_value = stats.ttest_1samp(a=data[str(column)], popmean=popmean)
    message='\nWe are now checking whether the average of column "'+str(column)+'" differs significantly from "'+str(popmean)+'"\n' + '\nIn this case the t-statistic score is: '+str(t_statistic)+'and the p-value is: '+str(round(float(p_value),4))+'.\n'
    if round(float(p_value),4) < P_value:
        message=+'The mean of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].mean())+', which is statistically significantly different from the test value of "'+str(popmean)+'".\n'
    else:
        message=+'The mean of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].mean())+', which is NOT statistically significantly different from the test value of "'+str(popmean)+'".\n'
    
    return message