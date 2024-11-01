def OneWayAnova(data,column1,column2,P_Value=0.05):
    from scipy.stats import f_oneway

    Groups=[]
    for i in data[str(column2)].unique():
        groupT=data[str(column1)][data[str(column2)] == i].reset_index(drop=True)
        Groups.append(groupT)
    if    len(Groups)==2:  stat,p=f_oneway(Groups[0],Groups[1])
    elif  len(Groups)==3:  stat,p=f_oneway(Groups[0],Groups[1],Groups[2])
    elif  len(Groups)==4:  stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3])
    elif  len(Groups)==5:  stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4])
    elif  len(Groups)==6:  stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5])
    elif  len(Groups)==7:  stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6])
    elif  len(Groups)==8:  stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7])
    elif  len(Groups)==9:  stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8])
    elif  len(Groups)==10: stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9])
    elif  len(Groups)==11: stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10])
    elif  len(Groups)==12: stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11])
    elif  len(Groups)==13: stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11],Groups[12])
    elif  len(Groups)==14: stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11],Groups[12],Groups[13])
    elif  len(Groups)==15: stat,p=f_oneway(Groups[0],Groups[1],Groups[2],Groups[3],Groups[4],Groups[5],Groups[6],Groups[7],Groups[8],Groups[9],Groups[10],Groups[11],Groups[12],Groups[13],Groups[14])
    means=''
    for g in Groups: means=means+str(g.mean())+', '
    if p <= P_Value: message='The one way Anova show that the mean of the dependent variable "'+str(column1)+'" differs significantly among the levels of "'+str(column2)+'" at a p_value equal to '+str(round(p,3))+' and a F value equal to '+str(round(stat,3))+'. The mean of the '+str(len(Groups))+' Groups are respectively: '+str(means[:-2])
    else:   message='The one way Anova show that the mean of the dependent variable "'+str(column1)+'" DOES NOT differs significantly among the levels of "'+str(column2)+'" at a p_value equal to '+str(round(p,3))+' and a F value equal to '+str(round(stat,3))+'. The mean of the '+str(len(Groups))+' Groups are respectively: '+str(means[:-2])
    return message
