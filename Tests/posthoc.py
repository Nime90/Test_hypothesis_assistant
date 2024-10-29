#PostHoc test
def posthoc_test(file_name,dep_var,ph_col):
    import scikit_posthocs as sp, pandas as pd ,numpy as np
    data=pd.read_excel(file_name+'.xlsx')
    print(sp.posthoc_ttest(data, val_col=str(dep_var), group_col=str(ph_col), p_adjust='holm'))

##### input data from here ####
x=0
while x==0:
    try:
        print('\npost hoc analysis (from Latin post hoc, "after this") consists of statistical analyses that were specified after the data were seen. They are usually used to uncover specific differences between three or more group means when an analysis of variance (ANOVA) test is significant. \n')
        file_name=input('Please insert here the excel file name: ')
        dep_var=input('Please specify here the column with the dependent variable: ')
        ph_col= input("If yes, please enter the name of the column for the posthoc test: " )

        try:
            posthoc_test(file_name,dep_var,ph_col)
            x=1
        except Exception as e: 
            print(e)
            x=0
    except Exception as e:
        print(e)
        x=0

input('\nPlease press enter to kill me!')