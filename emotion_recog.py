from tensorflow.keras.preprocessing.image import img_to_array
import imutils
import cv2
from tensorflow.keras.models import load_model
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import socket
import json
from collections import OrderedDict

import time

import threading

file_data = OrderedDict()
image_data = OrderedDict()

HOST = '127.0.0.1'
PORT = 4444
BUFSIZE = 1024
ADDR = (HOST, PORT)


class EmotionRecog():
    def __init__(self):
        # parameters for loading data and images
        detection_model_path = 'haarcascades/haarcascade_frontalface_default.xml'
        emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'

        # hyper-parameters for bounding boxes shape
        # loading models
        self.face_detection = cv2.CascadeClassifier(detection_model_path)
        self.emotion_classifier = load_model(emotion_model_path, compile=False)
        self.EMOTIONS = ["angry","disgust","scared","happy","sad","surprised","neutral"]
    
        # starting video streaming
        cv2.namedWindow('your_face')
        self.camera = cv2.VideoCapture(0)

        self.end = 0
        self.begin = 0
        self.last_label = None
    
    @staticmethod
    def sending(data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data.encode('utf-8'), ADDR)

    def get_frame(self):
        frame = self.camera.read()[1]
        #reading the frame
        frame = imutils.resize(frame,width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
        
        #canvas = np.zeros((250, 300, 3), dtype="uint8")
        frameClone = frame.copy()

        if len(faces) > 0:
            faces = sorted(faces, reverse=True,
            key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            result = self.end - self.begin

            if result <= 1:
                self.end = time.time()
                cv2.putText(frameClone, self.last_label, (fX, fY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                            (0, 0, 255), 2)
                
            else:
                self.begin = time.time()
                self.end = time.time()
        
                preds = self.emotion_classifier.predict(roi)[0]
                emotion_probability = np.max(preds)
                label = self.EMOTIONS[preds.argmax()]

                for (i, (emotion, prob)) in enumerate(zip(self.EMOTIONS, preds)):
                    # construct the label text
                    #text = "{}: {:.2f}%".format(emotion, prob * 100)

                    cv2.putText(frameClone, label, (fX, fY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                                (0, 0, 255), 2)

                    #if label == 'happy':
                    #    frame = self.get_frame()
                    #    ret, jpg = cv2.imencode('.jpg', frame)
                    #    image_data["is"] = "smile"
                    #    image_data["smile"] = jpg.tobytes()
                    #    smile = json.dumps(image_data, ensure_ascii=False, indent='\t')
                    #    self.sending(smile)

                    self.last_label = label

                    image_data["is"] = "emotions"
                    file_data["big_emotion"] = label
        
        
        
                    file_data[emotion] = int(prob*100)
                    data = json.dumps(file_data, ensure_ascii=False, indent='\t')

                self.sending(data)

        return frameClone

    def get_jpg_bytes(self):
        frame = self.get_frame()
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()

if __name__ == '__main__':
    emotion_recog = EmotionRecog()

    while True:
        frame = emotion_recog.get_frame()
       
        cv2.imshow('your_face', frame)
        #cv2.imshow("Probabilities", canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    camera.release()
    cv2.destroyAllWindows()