import face_recognition
import cv2
import sentimentDetection

cv2.destroyAllWindows()
cam = cv2.VideoCapture(0)
cv2.namedWindow("FaceRecognition")

counter = 0
previousEmotion = "unknow"
detectionEmotionPer = 1000
while True:
    ret, frame = cam.read()

    if not ret:
        continue
        print("Camera error.")

    rectangle = face_recognition.face_locations(frame)
    if len(rectangle) > 0:
        top, right, bottom, left = rectangle[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255))
    if counter % detectionEmotionPer == 0:
        img_filename = "faceRecognition.png"
        cv2.imwrite(img_filename, frame)
        emotion = sentimentDetection.createSentimentRequest(img_filename)
        if emotion:
            previousEmotion = emotion
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, previousEmotion, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow("FaceRecognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # time.sleep(0.5)

cam.release()
cv2.destroyAllWindows()

