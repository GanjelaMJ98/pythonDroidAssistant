import cv2
import time


cap = cv2.VideoCapture('111.mov')

cv2.namedWindow("Faces found",cv2.WINDOW_NORMAL)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (464, 848))



while(cap.isOpened()):
    cascPath = "haarcascade_frontalface_default.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    #image = cv2.imread(imagePath)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    if(len(faces) > 0):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        text = "Face not found."
        text1 = "Rotate the camera please."
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text,(250,250), font, 1,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(frame, text1, (250, 300), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Faces found", frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
