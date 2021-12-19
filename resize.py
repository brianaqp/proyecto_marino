if __name__ == '__main__':
    import os
    import imutils
    import cv2
    train_path ="data/train/water"
    validation_path = "data/validation/water"
    direcciones = [train_path ,validation_path]
    print('train: ', len(os.listdir(train_path)))
    print('validation: ', len(os.listdir(validation_path)))
    for path in direcciones:
        contador = 0
        print("Imprimiendo: ", path)
        for file in os.listdir(path):
            file = os.path.join(path,file)
            temp = cv2.imread(file)
            temp = cv2.resize(temp, (128,128))
            cv2.imwrite(file, temp)
            cv2.imshow('a', temp)
            print(temp.shape)
            # contador += 1