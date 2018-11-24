import cv2
class HaarDetector:
    frame = None
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = None
    grayImage = None
    faces = None
    
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)

    def detect(self, frame):
        self.frame = frame
        self.grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.faces = self.faceCascade.detectMultiScale(
            self.grayImage,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30)
            )
        #print("Found {0} faces!".format(len(self.faces)))
        return self.faces