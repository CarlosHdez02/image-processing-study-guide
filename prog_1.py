#pillow
import matplotlib
import numpy as np
import cv2
import matplotlib.image as plt_img
import matplotlib.pyplot as plt
from skimage import io , img_as_uint, img_as_float
'''
from PIL import Image
img = Image.open('yotsuba.png')
print(type(img)) #Not a numpy [] using pillow
print(img.format)
#img.show()
#Make the image a numpy array
img1 = np.asarray(img)
print(img1)
print(type(img1))'''
#with matplotlib

'''img = plt_img.imread('yotsuba.png')
img2 = plt_img.imread('myrgb.jpeg')
print(type(img))
print(img.shape)
print(img2.shape)
plt.imshow(img)
plt.show(img)
plt.colorbar'''

#skimage
'''
img = io.imread('myrgb.jpeg')
print(type(img))
print(img)
img_float = img_as_float(img)
print(img_float)'''
#OpenCV
img = cv2.imread('yotsuba.png',1)
img_gray = cv2.imread('yotsuba.png',0)
print(img.shape)
print(type(img))
cv2.imshow('yotsuba',img)
cv2.imshow('gray yotsuba',img_gray)
cv2.waitKey(0)#Gotta press the keyboard
cv2.destroyAllWindows  #This way i can have many images open
print(img)
print(img_gray) #array is different cuz there's no color