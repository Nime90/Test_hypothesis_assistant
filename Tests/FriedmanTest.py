#FriedmanTest
def FriedmanTest(file_name,groups,P_value):
    from scipy import stats
    import pandas as pd

    data=pd.read_excel(str(file_name)+'.xlsx')

    groups_list=groups.split(',')
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
##### input data from here ####
x=0
while x==0:
    try:
        print('\nFriedman test has two or more categorical independent variables (either with or without the interactions) and a single normally distributed interval dependent variable.\n')

        file_name=input('Please insert here the excel file name: ')
        groups=input('Please write here all the columns containing the column names to test, comma separated and NO SPACE (e.g. Col1,Col2,Col3...): ')
        P_value=float(input('Please insert here your P_value: '))

        try:
            result=FriedmanTest(file_name,groups,P_value)
            print(result)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('Please press enter to kill me!')