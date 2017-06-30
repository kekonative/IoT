import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('Euro_20_cent.jpg',0) # Kuva jonka piirteita etsitaan
img2 = cv2.imread('Malta_euro.jpg',0) # Kuva josta etsitaan

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Draw first 12 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:12],None,flags=2)
plt.imsave('vertaustulos.png', img3)
