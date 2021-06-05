import cv2
j=cv2.imread("joey.jpg")
c=cv2.imread("chandler.jpg")
cv2.imshow("Joey", j)
cv2.waitKey(3000)
cv2.destroyAllWindows()
cv2.imshow("Chandler", c)
cv2.waitKey(3000)
cv2.destroyAllWindows()
model=cv2.CascadeClassifier("haar.xml")
face1=model.detectMultiScale(j)
face2=model.detectMultiScale(c)
j=cv2.imread("joey.jpg")
c=cv2.imread("chandler.jpg")

x1=face1[0][0]
y1=face1[0][1]
x2=x1+face1[0][2]
y2=y1+face1[0][3]
j1=j[x1:x2,y1:y2]

x3=face2[0][0]
y3=face2[0][1]
x4=x1+face2[0][2]
y4=y1+face2[0][3]
c1=c[x3:x4,y3:y4]

cv2.imshow("joey", j)
if cv2.waitKey() == 13:
    cv2.destroyAllWindows()

cv2.imshow("Chandler", c)
if cv2.waitKey() == 13:
    cv2.destroyAllWindows()

l=cv2.resize(j1,(c1.shape[0],c1.shape[1]))
c[y3:y4,x3:x4] = l

cv2.imshow("Chandler", c)
if cv2.waitKey() == 13:
    cv2.destroyAllWindows()
