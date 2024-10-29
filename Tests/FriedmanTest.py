#FriedmanTest
def FriedmanTest(data,groups_list,P_value=0.05):
    from scipy import stats
    import pandas as pd

    n=len(groups_list)
    if   n==3: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])])
    elif n==4: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])], data[str(groups_list[3])])
    elif n==5: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])], data[str(groups_list[3])], data[str(groups_list[4])])
    elif n==6: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])], data[str(groups_list[3])], data[str(groups_list[4])], data[str(groups_list[5])])
    elif n==7: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])], data[str(groups_list[3])], data[str(groups_list[4])], data[str(groups_list[5])], data[str(groups_list[6])])
    elif n==8: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])], data[str(groups_list[3])], data[str(groups_list[4])], data[str(groups_list[5])], data[str(groups_list[6])], data[str(groups_list[7])])
    elif n==9: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])], data[str(groups_list[3])], data[str(groups_list[4])], data[str(groups_list[5])], data[str(groups_list[6])], data[str(groups_list[7])], data[str(groups_list[8])])
    elif n==10: s,p=stats.friedmanchisquare(data[str(groups_list[0])], data[str(groups_list[1])], data[str(groups_list[2])], data[str(groups_list[3])], data[str(groups_list[4])], data[str(groups_list[5])], data[str(groups_list[6])], data[str(groups_list[7])], data[str(groups_list[8])], data[str(groups_list[9])])

    if p<P_value: message='\nFriedman’s chi-square has a value of '+str(round(s,4))+' and a p-value of '+str(round(p,4))+' and is statistically significant.  Hence, there is evidence that the distributions of the '+str(n)+' groups are different.'
    else: message='\nFriedman’s chi-square has a value of '+str(round(s,4))+' and a p-value of '+str(round(p,4))+' and IS NOT statistically significant.  Hence, there IS NO evidence that the distributions of the '+str(n)+' groups are different.'
    return message
