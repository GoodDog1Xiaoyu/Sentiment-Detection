import requests
import cv2

access_key = "eb51b4818a964cb890462a95d327faef"
emotion_recognition_url = "https://eastus.api.cognitive.microsoft.com/face/v1.0/detect"
headers  = {'Ocp-Apim-Subscription-Key': access_key, "Content-Type": "application/octet-stream" }

def createSentimentRequest(image_path):
    image_data = open(image_path, "rb").read()
    # print(image_data)
    params = {
        'returnFaceAttributes': 'emotion'
    }

    response = requests.post(emotion_recognition_url, headers = headers, params = params, data = image_data)

    analysis = response.json()
    try:
        emotion = ""
        emotion_score = 0
        emotion_map = analysis[0]["faceAttributes"]["emotion"]
        for key in emotion_map.keys():
            if emotion_map[key] > emotion_score:
                emotion_score = emotion_map[key]
                emotion = key
    except Exception as e:
        return None
    return emotion
    # print(emotion, emotion_score)



