from pdf2image import convert_from_path
import glob,os
import os, subprocess

os.chdir('/Users/absvn/Desktop/folder_name/')

for file in glob.glob('*.pdf'):
    images = convert_from_path(file)
    
for i in range(len(images)):
    images[i].save('/Users/absvn/Desktop/folder_name/page'+ str(i) +'.jpg', 'JPEG')
