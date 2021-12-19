import sys
import cv2
import tensorflow as tf
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import os
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
import math

def same_size(path, file_shape):
    for file in os.listdir(path):
        if file == '.DS_Store': continue
        test = cv2.imread(path + "/" +file)
        x, y, _ = test.shape
        if x != file_shape and y != file_shape:
            return False
        return True

if __name__ == '__main__':
    physical_devices = tf.config.list_physical_devices('GPU')
    K.clear_session() # liberar el cache
    """Lo primero que se hace es confirmar que todas
       las imagenes son del mismo tamaño."""
    # para entrenamiento
    path = "data/train/brain"
    file_shape = 128
    if same_size(path, file_shape) != True:
        sys.exit(0)
    print("Todos los archivos de train son del mismo tamaño. ({})".format(file_shape))
    # para validacion
    path = "data/validation/brain"
    if same_size(path, file_shape) != True:
        sys.exit(0)
    print("Todos los archivos de validation son del mismo tamaño. ({})".format(file_shape))

    # Carpetas de informacion
    brain_coral = "/brain"
    # Parametros
    nombre_clases = ["Brain coral", 'Staghorn', 'sand', 'water']
    num_clases = len(nombre_clases)
    data_entrenamiento = "./data/train"
    data_validacion = "./data/validation"
    train_num_images = len(os.listdir(data_entrenamiento+brain_coral))
    validation_num_images = len(os.listdir(data_validacion+brain_coral))

    epocas = 100
    altura, longitud = 128, 128
    batch_size = 10 # imagenes que procesa en cada paso
    pasos = 70 // batch_size
    pasos_validacion = 40 // batch_size
    filtrosConv1 = 32
    filtrosConv2 = 64
    tamano_filtro1 = (3,3)
    tamano_filtro2 = (2,2)
    tamano_pool=(2,2)
    clases = len(nombre_clases)
    lr=0.05

    # pre procesamiento de las imagenes
    entrenamiento_datagen = ImageDataGenerator(
        rescale=1./255, # normalizado
        shear_range = 0.2, # imagen girada
        zoom_range = 0.2, # imagenes con zoom
        horizontal_flip = True # horizontal flip
    )

    validacion_datagen = ImageDataGenerator(
        rescale=1./255)

    imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(
        data_entrenamiento,
        target_size=(altura, longitud),
        batch_size=batch_size,
        class_mode="categorical")
    print(imagen_entrenamiento)
    imagen_validacion = validacion_datagen.flow_from_directory(
        data_validacion,
        target_size=(altura,longitud),
        batch_size=batch_size,
        class_mode="categorical")
    # Modelo
    modelo = Sequential()
    modelo.add(Convolution2D(filters=filtrosConv1,
                             kernel_size=tamano_filtro1,
                             padding="same",
                             input_shape=(longitud, altura, 3),
                             activation='relu'))
    modelo.add(MaxPooling2D(pool_size=tamano_pool))

    modelo.add(Convolution2D(filtrosConv2, tamano_filtro2, padding="same"))
    modelo.add(MaxPooling2D(pool_size=tamano_pool))

    modelo.add(Flatten())
    modelo.add(Dense(1000, activation='relu'))
    modelo.add(Dropout(0.35))
    modelo.add(Dense(500, activation='relu'))
    modelo.add(Dense(100, activation='relu'))
    modelo.add(Dense(clases, activation='softmax'))
    # compilacion del modelo
    modelo.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics='accuracy')

    modelo.fit(
        imagen_entrenamiento,
        steps_per_epoch=pasos,
        epochs=epocas,
        validation_data=imagen_validacion,
        validation_steps=pasos_validacion)

    directory = "./modelo"
    if not os.path.exists(directory):
        os.mkdir(directory)
    modelo.save("./modelo/modelo.h5")
    modelo.save_weights("./modelo/pesos.h5")