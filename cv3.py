import cv2
import numpy as np
j=cv2.imread("joey.jpg")
c=cv2.imread("chandler.jpg")
h=np.concatenate((j,c),axis=1)
cv2.imshow("u",h)
if cv2.waitKey(3000) == 13:
    cv2.destroyAllWindows()
