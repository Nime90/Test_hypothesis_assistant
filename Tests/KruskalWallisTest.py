def KruskalWallis(data,dep_var,ind_var,P_value=0.05):
    from scipy import stats
    from scipy.stats import f_oneway

    Groups=[]
    for i in data[str(ind_var)].unique():
        groupT=data[str(dep_var)][data[str(ind_var)] == i].reset_index(drop=True)
        Groups.append(groupT)
    if    len(Groups)==2:  stat,p=stats.kruskal(Groups[0],Groups[1])
    elif  len(Groups)==3:  stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2])
    elif  len(Groups)==4:  stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3])
    elif  len(Groups)==5:  stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4])
    elif  len(Groups)==6:  stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5])
    elif  len(Groups)==7:  stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6])
    elif  len(Groups)==8:  stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7])
    elif  len(Groups)==9:  stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8])
    elif  len(Groups)==10: stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9])
    elif  len(Groups)==11: stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10])
    elif  len(Groups)==12: stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11])
    elif  len(Groups)==13: stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11],Groups[12])
    elif  len(Groups)==14: stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11],Groups[12],Groups[13])
    elif  len(Groups)==15: stat,p=stats.kruskal(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11],Groups[12],Groups[13],Groups[14])
    means=''
    for g in Groups: means=means+str(g.mean())+', '
    if p <= P_value: message='\nThe Kruskal Wallis test shows that the mean of the dependent variable "'+str(dep_var)+'" differs significantly among the levels of "'+str(ind_var)+'" at a p_value equal to '+str(round(p,3))+' and a Chi-Squared value equal to '+str(round(stat,3))+'. The mean of the '+str(len(Groups))+' Groups are respectively: '+str(means[:-2])
    else:   message='\nThe Kruskal Wallis test shows that the mean of the dependent variable "'+str(dep_var)+'" DOES NOT differs significantly among the levels of "'+str(ind_var)+'" at a p_value equal to '+str(round(p,3))+' and a Chi-Squared value equal to '+str(round(stat,3))+'. The mean of the '+str(len(Groups))+' Groups are respectively: '+str(means[:-2])
    
    return message