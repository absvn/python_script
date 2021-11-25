# delete the rows which contains these values in the column 



import pandas
df = pandas.read_csv('input.csv')

bad_values = ['A00-B99','D50-D89','E00-E90','F00-F99','G00-G99','H00-H59','H60-H95','I00-I99','J00-J99','K00-K93',
           'K00-K95','L00-L99','M00-M99','N00-N99','O00-O99','P00-P96','Q00-Q99','R00-R99','S00-T98','U00-U99',
           'V01-Y99','Z00-Z99','0','O00-O9A','E00-E89','F01-F99','S00-T88','U00-U49','V00-Y99','V01-Y98']

print('There are ' + str(len(df)) + 'total rows')
df = df[~df['column_name'].isin(bad_values)]
df.to_csv('output.csv', index = False)
print('There are ' + str(len(df)) + ' rows left')
