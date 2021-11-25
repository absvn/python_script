from pdf2image import convert_from_path
images = convert_from_path('/Users/abhinavsingh/Desktop/folder_name/*.pdf')
 
for i in range(len(images)):
    images[i].save('/Users/abhinavsingh/Desktop/folder_name/page'+ str(i) +'.jpg', 'JPEG')
