# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:04:23 2023

@author: Svenja
"""

def get_content_df (df,base,colname,add=''):
    
    if type(base)==str:
        name=base+add
        df[name]=[seq.upper().count(base)/len(seq) for seq in df[colname]]
    if type(base)==list:
        for element in base:
            name=element+add
            df[name]=[seq.upper().count(element)/len(seq) for seq in df[colname]] 
            
def get_combined_content(df,bases,colname,add=''):
    name='all'+bases+add
    for i,seq in enumerate(df[colname]):
        count=0
        for base in bases:
            count+=seq.count(base)
        df.at[i,name]=count/len(seq)
        
def odds_dinuk(df,dn,colname,add=''):
    '''f(ApB)/f(A)*f(B) --> distribution by chance: 1'''
    name='odds'+dn+add
    df[name]=[(seq.upper().count(dn)/len(seq))/((seq.upper().count(dn[0])/len(seq))*seq.upper().count(dn[1])/len(seq)) for seq in df[colname]]
    

# def write_files(df,name):
#     df.to_excel(name+'RNA.xlsx')
    
#     get_content_df(df, ['CG','GC'],'Seq')
#     get_combined_content(df,'GC','Seq')
#     get_content_df(df, ['CG','GC'],'noCpG100',add='_100')
#     get_combined_content(df,'GC','noCpG100',add='_100')
#     get_content_df(df, ['CG','GC'],'noCpG50',add='_50')
#     get_combined_content(df,'GC','noCpG50',add='_50')
    
#     df=change_base(df, 'Seq', 'U', 'T')
#     df.to_excel(name+'.xlsx')
    
#     df_1=df.loc[:,['noCpG100','changes100']]
#     df_3=df.loc[:,['noCpG50','changes50']]

#     df_1.insert(0,'name100',[name+'_noCpG100' for name in df.iloc[:,0]])
#     df_3.insert(0,'name50',[name+'_noCpG50' for name in df.iloc[:,0]])
    
#     df_1=change_base(df_1, 'noCpG100', 'U', 'T')
#     df_3=change_base(df_3, 'noCpG50', 'U', 'T')
    
#     #get_content_df(df_1, ['CG','GC'],'hCpG1')
#     #get_combined_content(df_1,'GC','hCpG1')
#     #get_content_df(df_3, ['CG','GC'],'hCpG3')
#     #get_combined_content(df_3,'GC','hCpG3')
    
#     df_1.to_excel(name+'change100.xlsx')
#     df_3.to_excel(name+'change50.xlsx')