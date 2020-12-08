from matplotlib import pyplot as plt
from keras.preprocessing import image
import cv2
import numpy as np

def emotion_analysis(emotions):
    objects = ('Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral')
    y_pos = np.arange(len(objects))
 
    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')
    
    plt.show()

import face_recognition as fr

# 사진의 얼굴 몇개인지 확인
img = fr.load_image_file('./data/face_recognition_test2.jpg', mode="L") # 사진
face_locations = fr.face_locations(img)
print(len(face_locations))

from keras.models import load_model
model = load_model('facial_expression_recognition.h5')

# 얼굴들의 감정 확인
for (top, right, bottom, left) in face_locations:
    crop = img[top:bottom, left:right]
    crop = cv2.resize(crop, (48, 48))
 
    x = image.img_to_array(crop)
    x = np.expand_dims(x, axis = 0)
 
    x /= 255
 
    custom = model.predict(x)
    emotion_analysis(custom[0])
 
    x = np.array(x, 'float32')
    x = x.reshape([48, 48])
 
    plt.gray()
    plt.imshow(x)
    plt.show()
    