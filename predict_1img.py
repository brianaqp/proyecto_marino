import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import imutils
import cv2
import tensorflow as tf

modelo = "./modelo/modelo.h5"
pesos = "./modelo/pesos.h5"
modelo = load_model(modelo)
# modelo = tf.saved_model.load(modelo)
modelo.load_weights(pesos)
x_max, y_max = 128,128
def predict(file):
    x = load_img(file, target_size=(x_max, y_max))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = modelo.predict(x)
    result = array[0]
    print(result)
    answer = np.argmax(result)
    print(answer)
    if answer == 0:
        print("brain")
    elif answer == 1:
        print('staghorn')

def predict_realtime(file):
    x = img_to_array(file)
    x = np.expand_dims(x, axis=0)
    array = modelo.predict(x)
    print('asasdas', predict_classes)
    print(modelo.metrics_name)
    result = array[0]
    answer = np.argmax(result)
    if answer == 0:
        print("brain")
    elif answer == 1:
        print('staghorn')
    elif answer == 2:
        print('sand')
    elif answer == 3:
        print('water or fishes')

# predict("./data/validation/staghorn/images (4).jpg") # el modelo si predice y todo
# predict("./data/train/brain/images.jpg") # el modelo si predice y todo
predict("./data/train/water/val108.jpeg") # el modelo si predice y todo


