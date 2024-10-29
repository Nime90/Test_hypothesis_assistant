#Binomial Test
def BinomialTest(data,dep_var,pr=0.5, P_value=0.05,tails=2):
    import pandas as pd 
    from scipy.stats import binomtest
    pr=float(pr)
    column=dep_var
    successes = data[column].sum()
    trials = len(data[column])
    test_result=binomtest(successes, trials, pr, alternative='two-sided')
    p_v=test_result.pvalue
    message='We are now checking whether the proportion of successes (i.e. "1") on column "'+str(column)+'" differs significantly from "'+str(pr)+'"'+ 'In this case the  p-value is: '+str(round(float(p_v),4)*int(tails))+'.'
    if round(float(p_v),4)*int(tails) < P_value:
        message = message + 'The proportion of '+str(data[str(column)].unique()[1])+' in the variable "'+str(column)+'" for this particular sample is '+str(round((sum(data[str(column)])/len(data[str(column)]))*100,2))+'%'+', which is statistically significantly different from the hypothesized value of '+str(float(pr)*100)+'%'+'.'
    else:
        message = message + 'The proportion of '+str(data[str(column)].unique()[1])+' in the variable "'+str(column)+'" for this particular sample is '+str(round((sum(data[str(column)])/len(data[str(column)]))*100,2))+'%'+', which is NOT statistically significantly different from the hypothesized value of '+str(float(pr)*100)+'%'+'.'
    return message
