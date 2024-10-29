#OneSample Median-test
def OneSampleMediantest(data,column,popmean,P_value=0.05):
    from scipy.stats import wilcoxon

    w, p = wilcoxon(data[str(column)])
    message='\nWe are now checking whether the median of column "'+str(column)+'" differs significantly from "'+str(popmean)+'"\n' + '\nIn this case the t-statistic score is: '+str(w)+' and the p-value is: '+str(round(float(p),4))+'.\n'
    if round(float(p),4) < P_value:
        message=message+'The median of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].median())+', which is statistically significantly different from the test value of "'+str(popmean)+'".\n'
    else:
        message=message+'The median of the variable "'+str(column)+'" for this particular sample is '+str(data[str(column)].median())+', which is NOT statistically significantly different from the test value of "'+str(popmean)+'".\n'
    return message
