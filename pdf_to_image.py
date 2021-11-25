from pdf2image import convert_from_path
images = convert_from_path('/Users/absvn/Desktop/folder_name/input.pdf')
 
for i in range(len(images)):
    images[i].save('/Users/absvn/Desktop/folder_name/page'+ str(i) +'.jpg', 'JPEG')
