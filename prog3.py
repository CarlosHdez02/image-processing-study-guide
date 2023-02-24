from skimage import io, img_as_ubyte
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np


fig,axs=plt.subplots(2,3) #Dos renglones tres columnas



img = io.imread('pinguino.jpeg',as_gray=True)
#io.imshow(img)
print(img.shape)
print(type(img))
print(img[10:15,20:25])

num_mean = img.mean()
max_value = img.max()
min_value = img.min()

print(num_mean, '\n', max_value ,'\n', min_value)

flipL_R = np.fliplr(img)
flipU_D = np.flipud(img)
rotated = ndimage.rotate(img,45,reshape=False)
gaussian_filter_img = ndimage.gaussian_filter(img,sigma=3)

axs[0,0].imshow(img, cmap="hsv")
axs[0,1].imshow(flipL_R, cmap="Greys")
axs[1,0].imshow(flipU_D, cmap="Blues")
axs[1,1].imshow(rotated)
axs[0,2].imshow(gaussian_filter_img) #Renglon 0, columna 1
plt.show()