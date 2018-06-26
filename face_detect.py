#!usr/bin/python

import cv2,random

face_cascade=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
cap=cv2.VideoCapture(0)
while cap.isOpened():
	status,img=cap.read()
	grayimage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(grayimage,1.15,5)
	for(x,y,w,h) in faces:
		f=cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img,"Face",(x,y),f,3,(100,23,200))
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray=grayimage[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
		x=random.random()
		y=str(x)[2:6]
		cv2.imwrite('img'+y+'.jpg',img)		
		cv2.imshow("imgw",img)
      		if cv2.waitKey(1) == 27 :
			break
cv2.destroyAllWindows()
cap.release()


