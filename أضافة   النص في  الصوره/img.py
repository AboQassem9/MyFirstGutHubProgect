import numpy as np
import cv2

image = cv2.imread('n.jpg',cv2.IMREAD_UNCHANGED)

position = (10,50)
cv2.putText(
     image,
     "HI TEATCHER BELAL I AM MOHAMMED NAJEEB ALTRIKI "
     "THIS MY PROJECT FOR YOU ",
     position,
     cv2.FONT_HERSHEY_SIMPLEX,
     1,
     (80, 80, 100, ),
     3)
cv2.imwrite('outut.jpg', image)