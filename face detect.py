import cv2 as cv 

# img = cv.imread('img.jpg')

# grey = cv.cvtColor(img, cv.COLOR_BGR2RGB)

haar_cascade = cv.CascadeClassifier('haarcascade.xml')


capture = cv.VideoCapture(0)
while True:
	isTrue, f =capture.read()

	face_rect = haar_cascade.detectMultiScale(f, scaleFactor=1.1,minNeighbors=3)

	print(len(face_rect))

	for (x,y,w,h) in face_rect:
		cv.rectangle(f, (x,y) ,(x+w,y+h), (0,255,0), thickness=2)

		cv.putText(f,str(len(face_rect))+"Face Detected",(x,y),cv.FONT_HERSHEY_DUPLEX,1.0,(255,0,0),1)


	cv.imshow('detected',f)

	if cv.waitKey(1) & 0xFF==ord('d'):
		break

	cv.waitKey(5)
	# cv.destroyAllWindows()
