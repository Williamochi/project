from PIL import Image
import numpy as np

# use PIL library
img = Image.open('lenna.jpg').convert('RGB')
img, cb, cr = img.convert('YCbCr').split()
img = np.array(img).astype(np.float32) / 255.
print(img[:48,:48])

# use formula
def rgb_to_y(img_array):
    # formula is from wikipedia
    R,G,B = img_array[0], img_array[1], img_array[2]
    return 16. + (65.481 * R + 128.553 * G + 24.966 * B) / 255.

img2 = Image.open('lenna.jpg').convert('RGB')
img2 = np.array(img2).transpose((2, 0, 1)).astype(np.float32) # c,h,w
img2 = rgb_to_y(img2) / 255.
print(img2[:48,:48])