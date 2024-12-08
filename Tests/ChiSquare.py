#Chisquare
def Chisquare(data,ind_var,dep_var,P_value=0.05):
    import scipy.stats as stats
    import numpy as np, pandas as pd
    from scipy.stats import chi2_contingency

    group1=data[str(dep_var)][data[str(ind_var)]>0].reset_index(drop=True)
    group2=data[str(dep_var)][data[str(ind_var)]==0].reset_index(drop=True)
    observed_data=group1.value_counts().sort_index()
    expected_data=group2.value_counts().sort_index()
    o_d='['
    for o in observed_data:o_d=o_d+str(o)+', '
    o_d=o_d+']'
    o_d=o_d.replace(', ]',']')
    e_d='['
    for e in expected_data:e_d=e_d+str(e)+', '
    e_d=e_d+']'
    e_d=e_d.replace(', ]',']')

    datatot_e=[]
    datatot_o=[]
    for e in expected_data: datatot_e.append(e)
    for o in observed_data: datatot_o.append(o)
    datatot=[datatot_o,datatot_e]

    stat, p, dof, expected = chi2_contingency(datatot)

    message='We are now checking whether there is relationhip between the values in the column "'+str(dep_var)+'" when "'+str(ind_var)+'" is equal to "1" : '+str(o_d)+' and the values in the same column when "'+str(ind_var)+'" is equal to "0" : '+str(e_d)+'.'+' In this case the  p-value is: '+str(round(float(p),3))+'.' + ' Chi_square_test_statistic is : ' + str(round(stat,3))+'.'+ ' Degrees of freedom are: '+str(dof)
    if round(float(p),3) < P_value: 
        message=message + '. These results indicate that there is statistically significant relationship between the variable "'+str(ind_var)+'" and "'+str(dep_var)+'".'
    else:  message=message +'. These results indicate that there is NOT statistically significant relationship between the variable "'+str(ind_var)+'" and "'+str(dep_var)+'".'
    
    return message

