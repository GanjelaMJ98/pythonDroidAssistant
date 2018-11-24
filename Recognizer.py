import cv2

def searchFace(FrameCharacter,faces):
    for (x, y, w, h) in faces:
        if((x > FrameCharacter["X0"]) and (y > FrameCharacter["Y0"])) and ((x + w <FrameCharacter["X1"] ) and (y + h<FrameCharacter["Y1"])):
            #print("Center")
            return "Center"
        if(x < FrameCharacter["X0"]):
            #print("Left")
            return "Left"
        if(x+w > FrameCharacter["X1"]):
            #print("Right")
            return "Right"

def drawRectangle(frame, faces):
    if (len(faces) > 0):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            distance = 150 - w / 2
            if (distance < 50):
                distance = (400 - w) / 4
            text = "S: {0} sm".format(distance)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, text, (x, y), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            return int(distance)


class FrameCharacter:
    frame = None
    character = dict()
    def __init__(self,frame):
        self.frame = frame
    def character(self):
        height, width = self.frame.shape[:2]
        self.character = {
            "lenght": 200,
            "center_x" : int(width/2),
            "center_y" : int(height/2),
            "height" : height,
            "width" : width,
            "X0" : int(width/2) - 200,
            "Y0" : int(height/2) - 200,
            "X1" : int(width/2) + 200,
            "Y1" : int(height/2) + 200
        }
        return self.character

