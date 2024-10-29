#NonParametricCorrelation
x=0
while x==0:
    try:
        from scipy.stats import pearsonr
        from scipy import stats
        import pandas as pd
        print('\nA Spearman correlation is used when one or both of the variables are not assumed to be normally distributed and interval (but are assumed to be ordinal). The values of the variables are converted in ranks and then correlated. \n')
        file_name=input('Please insert here the excel file name: ')
        col1=input('Please insert the name of the first variable: ')
        col2=input('Please insert the name of the second variable: ')
        P_value=float(input('Please insert here your P_value: '))

        data=pd.read_excel(str(file_name)+'.xlsx')

        corr, p = stats.spearmanr(data[str(col1)], data[str(col2)])
        prop=(corr*corr)*100

        if round(p,4)<round(P_value,4): res='is'
        else: res='IS NOT'

        print('\nThe Spearmanr correlation score between the two columns is '+str(round(corr,4))+'. ')
        print('\nSince the p_value is '+str(round(p,4))+' this correlation '+str(res)+' statistically significant!')
        x=1
    except Exception as e: 
        print(e)
        x=0
input('\nPlease press Enter to kill me!')