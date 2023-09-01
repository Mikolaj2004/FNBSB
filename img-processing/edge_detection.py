import cv2
import os

#Funkcja przetwarza obrazy za pomocą algorytmu Canny

def edge_detection(filepath,output_path):

    filename = os.path.basename(filepath)

    img = cv2.imread(filepath)
    blur = cv2.GaussianBlur(img, (5,5), 0)
    imageOutput = cv2.Canny(blur, threshold1=80, threshold2=170)

    cv2.imwrite(os.path.join(output_path,filename), imageOutput)

    return imageOutput