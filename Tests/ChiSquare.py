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

##### input data from here ####
#x=0
#while x==0:
#    try:
#        print('A chi-square test is used when you want to see if there is a relationship between two categorical variables.\n')
#        file_name=input('Please insert here the excel file name: ')
#        column=input('Please select one of the column you want to test (it must contain only 0,1 value. if this is not the case please fix the data before running this): ')
#        column2=input('Please select the second categorical column you want to test: ')
#        P_value=float(input('Please insert here your P_value: '))
#        try:
##            result=Chisquare(file_name,column,column2,P_value)
#            print(result)
##            x=1
#        except Exception as e: 
#            print(e)
#            x=0
#    except Exception as e:
#        print(e)
#        x=0

#input('\nPlease press enter to kill me!')