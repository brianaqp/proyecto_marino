if __name__ == '__main__':
    import cv2
    import time
    import keyword
    import imutils
    import os
    contador = 0
    contador2 = 0
    directory = "C:/Users/brian/PycharmProjects/proyecto_marino10/data/water"
    cap = cv2.VideoCapture('video_para_elagua.mp4')
    os.chdir(directory)
    cap.read()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            # img = cv2.resize(frame (128,128))
            cv2.imshow("frame", frame)
            # cv2.imwrite("val"+str(contador)+".jpeg", img)
            contador += 1
                # cv2.imwrite("val"+str(contador)+".jpeg", frame)
            if contador == 200:
                print(contador)
                cv2.imwrite("val"+str(contador2)+".jpeg", frame)
                contador2 += 1
                contador = 0
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
