import cv2
import numpy
import math
cn=numpy.ones((720,720,3))
def outer(cn):
    cn=numpy.ones((720,720,3))
    for x in range(280,360):
        cn=cv2.circle(cn , (360,360), x, [0,0,255] )
    for x in range(120,200):
        cn=cv2.circle(cn , (360,360), x, [0,0,255] )
    cn=cv2.circle(cn , (360,360), 120 , [255,0,0] ,-1)
    return(cn)
    def star(cn):
    R1 = 120
    R2 = 40
    v=[]
    vi=[]
    for n in range(0,5):
        x1 = R1*math.cos(math.radians(90+n*72))
        y1 = R1*math.sin(math.radians(90+n*72))
        x2 = R2*math.cos(math.radians(126+n*72))
        y2 = R2*math.sin(math.radians(126+n*72))
        vi.append([int(x2)+360,int(y2)+360])
        v.append([int(x1)+360,int(y1)+360])
    
    t1=numpy.array([v[2],v[0],vi[3]])
    t2=numpy.array([v[1],v[3],vi[4]])
    t3=numpy.array([v[2],v[4],vi[0]])

    cn=cv2.fillPoly(cn,pts=[numpy.array(t1)], color=[255,255,255])
    cn=cv2.fillPoly(cn,pts=[numpy.array(t2)], color=[255,255,255])
    cn=cv2.fillPoly(cn,pts=[numpy.array(t3)], color=[255,255,255])
    return(cn)
    # view
cn=outer(cn)
a=star2(cn)
cv2.imshow("Animation",a)
if cv2.waitKey()==13:
    cv2.destroyAllWindows()
    #animation
while True:
    cn=outer(cn)
    a=star(cn)
    cv2.imshow("Animation",a)
    cv2.waitKey(55)
    cn=cv2.rotate(cn, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Animation",cn)
    cv2.waitKey(55)
    cn=cv2.rotate(cn, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Animation",cn)
    cv2.waitKey(55)
    cn=cv2.rotate(cn, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Animation",cn)
    cv2.waitKey(55)
