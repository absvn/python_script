from PIL import Image

for i in range(12):
    i = str(i)
    img = Image.open('/Users/absvn/Desktop/rgb_to_grayscale/page'+str(i)+'.jpg')
    imgGray = img.convert('L')
    imgGray.save('/Users/absvn/Desktop/rgb_to_grayscale/new'+str(i)+'.jpg')
