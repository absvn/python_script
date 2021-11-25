import os
import pandas as pd
cwd = os.path.abspath('/Users/abhinavsingh/Desktop/amount/icd_preds/') 
files = os.listdir(cwd)  

df = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        print(file)
        df = df.append(pd.read_csv(file, encoding='utf-8'), ignore_index=True) 
df.to_csv('combine_preds.csv', index= False)
