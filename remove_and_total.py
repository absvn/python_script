for i in folder:
    route = '/Users/absvn/Desktop/ipa_react/processed/'+str(i)+'/main/*'
    total = 0
    for file in glob.glob(route):
        total += 1
    if total != 12:
        print('removed :', str(i))
        folder.remove(i)
    else:
        pass
    
    print(str(i), ':', + total)
