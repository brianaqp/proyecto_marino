import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import imutils
import cv2

# parametros
x_max, y_max = 128, 128
kernel_size_x = 200
kernel_size_y = 200
clases = ['brain', 'stra']
# ----------
modelo = "./modelo/modelo.h5"
pesos = "./modelo/pesos.h5"
modelo = load_model(modelo)
modelo.load_weights(pesos)

def pause(file):
    print(file.shape)
    cv2.imshow('a', file)
    cv2.waitKey(0)
    cv2.imwrite("./prueba56.jpeg", file)
    cv2.destroyAllWindows()


def predict(file, realtime):
    if realtime == True:
        x = file
    elif realtime == False:
        x = load_img(file, target_size=(x_max, y_max))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = modelo.predict(x)
    result = array[0]
    answer = np.argmax(result)
    return answer

def draw(frame, x1, x2, y1, y2, text, color):
    frame = cv2.rectangle(frame,
                  (x1, y1),
                  (x2, y2),
                  color, 3)
    cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

# predict("prueba56.jpeg") # el modelo si predice y todo

process = True
# cap = cv2.VideoCapture('./data/test/video.mp4')
cap = cv2.VideoCapture('prueba.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    altura, longitud = frame.shape[0], frame.shape[1]
    x_times = longitud // kernel_size_x
    y_times = altura // kernel_size_y
    x_actual, y_actual = 0, 0
    if ret == True:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # while process:
        # predicted_image = frame[y_actual:y_actual + kernel_size_y, x_actual:x_actual + kernel_size_x]  # altura, longitud
        y1, y2 = int((altura*0.40)), int((altura*0.80))
        x1, x2 = int((longitud*0.40)), int((longitud*0.80))
        print(x1,x2,y1,y2)
        print(frame.shape)
        predicted_image = frame[y1:y2, x1:x2]  # altura, longitud
        # pause(predicted_image)
        cv2.rectangle(frame,
                       (x1,y1),
                       (x2,y2),
                       (0,255,5),3)
        image_resized = cv2.resize(predicted_image, (x_max,y_max))
        answer = predict(image_resized, True)
        cv2.imshow('sdfa', predicted_image)
        print(answer)
        color = (255,255,255)
        if answer == 0:
            text = 'branching'
            color = (0,0,255) # branching
        if answer == 1:
            color = (0,255,0) # water
            text = 'brain'
        if answer == 2:
            color = (143,205,55) # sand
            text = 'sand or rocks'
        if answer == 3:
            color = (255, 0, 0) # water or sea fishes
            text = 'water or fishes'
        draw(frame, x1, x2, y1, y2, text, color)
            # if answer == 2:
            #     draw(frame, 'staghorn', (0,0,255))
        cv2.imshow("frame", frame)
        print(modelo.history())
        # x_actual += kernel_size_x
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break