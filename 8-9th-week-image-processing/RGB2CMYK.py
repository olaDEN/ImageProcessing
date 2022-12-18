from PIL import Image

image = Image.open('rgbImg.jpg')

if image.mode == 'RGB':
    cmyk = image.convert('CMYK')
    cmyk.show()

else:
    rgb = image.convert('RGB')
    cmyk = rgb.convert('CMYK')
    cmyk.show()


