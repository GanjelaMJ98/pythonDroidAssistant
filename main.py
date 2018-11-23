import cv2
import HaarDetector as Detector
from Recognizer import searchFace, drawRectangle, FrameCharacter



if __name__ == "__main__":
    cap = cv2.VideoCapture("11.mp4")
    cv2.namedWindow("Faces found",cv2.WINDOW_NORMAL)
    font = cv2.FONT_HERSHEY_SIMPLEX
    detector = Detector.HaarDetector()

    while(1):
        #Получаем кадр
        ret, frame = cap.read()
        #Характеристики кадра
        FC = FrameCharacter(frame)
        frameCharacter = FC.character()

        #Область определения лица
        cv2.rectangle(frame, (int(frameCharacter["X0"]), int(frameCharacter["Y0"])), (int(frameCharacter["X1"]), int(frameCharacter["Y1"])),(255, 0, 0), 2)


        faces = detector.detect(frame)
        drawRectangle(frame,faces)

        if(searchFace(frameCharacter,faces)==True):
            cv2.putText(frame, "STOP ROTATING", (250, 250), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            text = "Face not found."
            text1 = "Rotate the camera, please."
            cv2.putText(frame, text, (250, 250), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, text1, (250, 300), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("Faces found", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

