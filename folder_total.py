for i in folder:
    route = '/Users/absvn/Desktop/ipa_react/processed/'+str(i)+'/main/*'
    total = 0
    for file in glob.glob(route):
        total += 1
    print(str(i),':', + total)
    
    # total of the folders inside the folder, nested folder 
