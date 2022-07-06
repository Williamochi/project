from PIL import Image
img = Image.open("lenna.jpg")
width, height = img.size

for x in range(width):
    for y in range(height):
        rgb = img.getpixel((x,y))
        rgb = (255 - rgb[0],  # R
                255 - rgb[1],  # G
                255 - rgb[2])  # B
        img.putpixel((x,y), rgb)

img.show()