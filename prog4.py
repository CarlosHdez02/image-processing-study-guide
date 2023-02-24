import matplotlib
from skimage import io,restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk
import matplotlib.pyplot as plt
from skimage.transform import resize
#Creating figure
fig,axs = plt.subplots(2,2)

#Opening image
img = io.imread('ana.jpeg')
cel_img = io.imread('celulas.jpeg')
gray_img = io.imread('ana.jpeg',as_gray=True)
#ent_img = entropy(img,disk(10))

#Manipulating image
#rescaled_img =  rescale(img,(1/4),anti_aliasing=True)
#resized_img = resize(img, (200,200))
#downscaled_img = downscale_local_mean(img,(4,4))



#Shape of image
print(img.shape)

#Showing img
axs[0,0].imshow(img), axs[0,0].set_ylabel('Original img')
axs[0,1].imshow(gray_img,cmap='gray'), axs[0,1].set_ylabel('Gray img')
#axs[1,0].imshow(ent_img)
axs[1,1].imshow(img,cmap='gray'),axs[1,1].set_ylabel('Roberrts')
plt.show()