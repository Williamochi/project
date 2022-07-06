from PIL import Image

image = Image.open('lenna.jpg')
pixel = image.load()
width = image.size[0]
height = image.size[1]
for x in range(width):
    for y in range(height):
        r, g, b = pixel[x, y]
