"""
Background removal code
"""
import numpy as np
from scipy import signal
from PIL import Image


def load_image(path):
    return np.asarray(Image.open(path))/255.0

def save(path, img):
    tmp = np.asarray(img*255.0, dtype=np.uint8)
    Image.fromarray(tmp).save(path)

def denoise_image(inp):
    # estimate 'background' color by a median filter
    bg = signal.medfilt2d(inp,11)
    save('images/background.png', bg)

    # compute 'foreground' mask as anything that is significantly darker than
    # the background
    mask = inp < bg - 0.1
    save('images/foreground_mask.png', mask)

    # return the input value for all pixels in the mask or pure white otherwise
    return np.where(mask, inp, 1.0)


image = Image.open('images/sample_DL.jpg')
image = image.convert('L') # convert image to grayscale
new_image = image.resize((832, 536))  
new_image.save('images/sample_DL_1.jpg')
inp_path = 'images/sample_DL_1.jpg'
out_path = 'images/output.png'

inp = load_image(inp_path)
out = denoise_image(inp)

save(out_path, out)
