# import scipy.misc as sci1
# from scipy.misc import imread, imsave, imresize
# from scipy.misc import imresize
import imageio.v2 as imageio
from imageio import imread, imsave  
# img = sci1.imread("./0.jepg")
# img = imread("0.jpg")
# print(img.dtype, img.shape)
# img_tint = img*[1,0.45,0.3]
# imsave("./cropin.jpg", img_tint)
img =imread('0.jpg') # path of the image
print(img.dtype, img.shape)
# Tinting the image
img_tint = img * [1, 0.45, 0.3]
# Saving the tinted image
imsave('./ cat_tinted.jpg', img_tint)
# Resizing the tinted image to be 300 x 300 pixels
img_tint_resize = imresize(img_tint, (300, 300))
# Saving the resized tinted image
imsave('./ cat_tinted_resized.jpg', img_tint_resize)
# print(sci1)
# Cannot handle this data type