import cv2
import HaarDetector as Detector
from Recognizer import searchFace, drawRectangle, FrameCharacter
import Turner


if __name__ == "__main__":
    cap = cv2.VideoCapture(0) # now from camera. For Video input his name
    cv2.namedWindow("Faces found",cv2.WINDOW_NORMAL) #print in command line
    font = cv2.FONT_HERSHEY_SIMPLEX
    detector = Detector.HaarDetector() 
    turner = Turner.Turner()
    i = 0
    pause = 0
    turn_cnt = 0
    while(1):
        pause += 1
        i+=1

        if turn_cnt >= 360:
            print("___________________MAN NOT FOUND__________________")
            quit()
        #Получаем кадр
        ret, frame = cap.read()
        #Характеристики кадра
        FC = FrameCharacter(frame)
        frameCharacter = FC.character()

        #Область определения лица
        cv2.rectangle(frame, (int(frameCharacter["X0"]), int(frameCharacter["Y0"])), (int(frameCharacter["X1"]), int(frameCharacter["Y1"])),(255, 0, 0), 2)

        faces = detector.detect(frame)
        #print("Found {0} faces!".format(len(faces)))
        distance = drawRectangle(frame,faces)
        
            #cv2.putText(frame, "STOP ROTATING", (250, 250), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        #else:
            #text = "Face not found."
            #text1 = "Rotate the camera, please."
            #cv2.putText(frame, text, (250, 250), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            #cv2.putText(frame, text1, (250, 300), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        if pause >= 80:
            if i >= 40:
                if(len(faces) != 0):
                    if(searchFace(frameCharacter,faces) == "Center"):
                        turner.go()
                        if int(distance) <= 40:
                            print("STOOOOOP")
                            quit()
                    elif(searchFace(frameCharacter,faces) == "Left"):
                        turn_cnt += turner.rotate_left()
                    elif(searchFace(frameCharacter,faces) == "Right"):
                        turn_cnt += turner.rotate_right()
                    else:
                        print("hz")
                else:
                    turn_cnt += turner.rotate_right()
                i=0      

        cv2.imshow("Faces found", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

