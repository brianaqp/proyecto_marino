import os
import numpy as np
import cv2
clase = 'staghorn'
path_train = './data/train/' + clase
path_validation = './data/validation/' + clase
#
dst_train = './data/water_removed/train/'
dst_validation = './data/water_removed/validation/'
#
low_color = [0,0,0]
high_color =[60,255,255]
max_size = 128
def remove_color(low_color, high_color, img):
    hsv_blue = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # blue range
    lower_blue = np.array(low_color)
    upper_blue = np.array(high_color)
    # Define a mask ranging from lower to uppper
    mask = cv2.inRange(hsv_blue, lower_blue, upper_blue)
    # Do masking
    res = cv2.bitwise_and(img, img, mask=mask)
    return res


for file in os.listdir(path_train):
    img = cv2.imread(path_train + '/' + file)
    img_2 = remove_color(low_color, high_color, img)
    cv2.imwrite(dst_train + clase + '/' + file, img_2)

for file in os.listdir(path_validation):
    img = cv2.imread(path_validation + '/' + file)
    img_2 = remove_color(low_color, high_color, img)
    cv2.imwrite(dst_validation + clase + '/' + file, img_2)

# cap = cv2.VideoCapture('./video_para_elagua.mp4')
# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret == True:
#         hsv_blue = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         # blue range
#         lower_blue = np.array([0, 0, 0])
#         upper_blue = np.array([50, 255, 255])
#         mask = cv2.inRange(hsv_blue, lower_blue, upper_blue)
#         # Do masking
#         blue = cv2.bitwise_and(frame, frame, mask=mask)
#         cv2.imshow('b', frame)
#         cv2.imshow('a',blue)
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break

# img = cv2.imread('./data/train/water/val3.jpeg')
# print(img.shape[0])