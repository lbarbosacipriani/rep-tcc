import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.filters.edges import sobel
from skimage.segmentation import active_contour
from skimage import io
import cv2 
#img = data.astronaut()
#img = rgb2gray(img)
img = io.imread("brown2.png")
#video=cv2.VideoCapture("videos/v1_Trim.mp4")
#img=rgb2gray(img)

 
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img_gray=sobel(img_gray)
img_gray=cv2.GaussianBlur(img_gray,(7,7),0)
#img_gray=cv2.threshold(img_gray,5,255,cv2.THRESH_BINARY)

s = np.linspace(0, 2*np.pi, 400)
r = 128 + 123*np.sin(s) # eixo y
c = 240 + 123*np.cos(s) # eixo x
init = np.array([r, c]).T

snake = active_contour(img_gray,
                     init, alpha=0.1, beta=10, gamma=0.001)

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img_gray, cmap=plt.cm.gray)
ax.plot(init[:, 1], init[:, 0], '--r', lw=3)
ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
plt.show()
