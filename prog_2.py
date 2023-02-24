from PIL import Image
from cv2 import imshow
from matplotlib import image

my_img = Image.open('yotsuba.png')
print(type(my_img))
print(my_img.size)
small_img = my_img.resize((400,300))
small_img.save('/Users/carloshernandez/Desktop/image/small_yotsuba.png')
my_img.thumbnail((200,300))
my_img.save('/Users/carloshernandez/Desktop/image/thumbtsuba.png')
imshow