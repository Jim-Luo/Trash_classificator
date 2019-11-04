import base64

import cv2
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


def ImageToMatrix(strPath):
    img = cv2.imread(strPath)
    img = cv2.resize(img, (150, 200))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_matrix = img_to_array(img)
    img_matrix_normalized = img_matrix / 255
    return img_matrix_normalized


def PredictGarbageType(strImg):
    strImgBin = base64.b64decode(strImg)
    fImg = open("temp.jpg", "wb")
    fImg.write(strImgBin)
    imgMatrix = ImageToMatrix("temp.jpg")
    model = load_model("model.h5")
    lsImg = list()
    lsImg.append(imgMatrix)
    predict_images = np.array(lsImg, dtype="float")
    predictions = model.predict_classes(predict_images)
    return predictions[0]


'''
Garbage type
0: cup
1: book
2: plastic wrapper
3: bottle
4: paper
5: trash
'''