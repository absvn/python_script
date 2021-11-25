# prints all file inside the folder

import glob, os
os.chdir("/Users/absvn/Desktop/tataaig_ipa_all_doc/")
for file in glob.glob('*.pdf'):
    print(file)
