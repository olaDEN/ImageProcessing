from PIL import Image
from PIL import ImageFilter

# Load the image in greyscale
img = Image.open('spring.jpg')

bl,gr,rd=img.split()

sharpBl = bl.filter(ImageFilter.SHARPEN)
sharpGr = gr.filter(ImageFilter.SHARPEN)
sharpRd = rd.filter(ImageFilter.SHARPEN)

result = Image.merge('RGB',(sharpBl,sharpGr,sharpRd))

# Show the sharpened images
result.show()
