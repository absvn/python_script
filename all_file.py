# prints all file inside the folder

import glob, os
os.chdir("/Users/abhinavsingh/Desktop/tataaig_ipa_all_doc/")
for file in glob.glob('*.pdf'):
    print(file)
