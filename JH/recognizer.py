from matplotlib import pyplot as plt
from keras.preprocessing import image
from PIL import Image
import cv2
import numpy as np
import os


def emotion_analysis(emotions):
    objects = ('Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise',
               'Neutral')
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')

    plt.show()


import face_recognition as fr

# url로 다운로드
url = "https://img.etoday.co.kr/pto_db/2018/01/600/20180103051731_1171674_600_743.jpg"
os.system("curl " + url + " > test.jpg")

# 사진의 얼굴 몇개인지 확인
img = fr.load_image_file('test.jpg')  # 사진
im = Image.open('test.jpg')
face_locations = fr.face_locations(img)
print(len(face_locations))

# from keras.models import load_model
# model = load_model('facial_expression_recognition.h5')

cnt = 1

# 얼굴들의 감정 확인
for (top, right, bottom, left) in face_locations:
    cropImage = im.crop((left, top, right, bottom))
    cropImage.save('test-crop.jpg')
    # crop = img[top:bottom, left:right]
    # crop.save('people' + str(cnt) + ".jpg")

    # crop = cv2.resize(crop, (48, 48))

    # x = image.img_to_array(crop)
    # x = np.expand_dims(x, axis=0)

    # x = np.array(x, 'float32')
    # x = x.reshape([48, 48, 3])
    # cv2.imwrite('people' + str(cnt) + ".jpg", x)
    # cnt += 1

    # x /= 255

    # custom = model.predict(x)
    # emotion_analysis(custom[0])

    # plt.gray()
    # plt.imshow(x)
    # plt.show()
