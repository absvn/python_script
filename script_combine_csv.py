import os
import pandas as pd
cwd = os.path.abspath('/Users/absvn/Desktop/folder_name/') 
files = os.listdir(cwd)  

df = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        print(file)
        df = df.append(pd.read_csv(file, encoding='utf-8'), ignore_index=True) 
df.to_csv('combine_output.csv', index= False)
