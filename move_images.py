# moving image from inside the folder

# there are folders inside the react folder so we need to take those folders inside the list to iterate over it

import os, glob, shutil
folder = []
os.chdir('/Users/abhinavsingh/Desktop/react/')
for file in glob.glob('*'):
    folder.append(file)
print(folder)


# there are folder inside the main folder so we need to take those forlders inside the list to iterate over it

in_folder = []
os.chdir('/Users/abhinavsingh/Desktop/react/etc/main/')
for i in glob.glob('*'):
    in_folder.append(i)
print(in_folder)
len(in_folder)

# main code begins from here

for i in folder:
    for j in in_folder:
        source = '/Users/abhinavsingh/Desktop/react/'+str(i)+'/main/'+str(j)+'/'
        destination = '/Users/abhinavsingh/Desktop/image_data/'+str(j)+'/' 
  
        files = os.listdir(source)
  
        for f in files:
            shutil.move(source + f, destination + f)
       
# here image_data folder has many folder inside it so it will match the folder and shift the data to that particular folder
