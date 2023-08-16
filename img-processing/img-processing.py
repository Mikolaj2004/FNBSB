import cv2
import os
import glob
from matplotlib import pyplot as plt
import numpy as np

#Definicja funkcji do detekcji krawędzi za pomocą algorytmu Canny

def edge_detection(filepath):

    filename = os.path.basename(filepath)

    img = cv2.imread(filepath)
    blur = cv2.GaussianBlur(img, (5,5), 0)
    imageOutput = cv2.Canny(blur, threshold1=80, threshold2=170)

    cv2.imwrite(os.path.join(output_path,filename), imageOutput)

    Count(imageOutput,filename,10)


#Funkcja obliczająca ziarnistość na podstawie zdjęcia z zastosowanym algorytmem Canny

def Count(imageOutput,filename,iterations):

    for i in range(iterations):
        result = [0 for _ in range(iterations)]

        line = np.zeros_like(imageOutput,dtype=int, order='K')
        line = line.astype(np.uint8)

        columnsNumber = line.shape[1]
        rowsNumber = line.shape[0]
    
        startX = np.random.randint(0, columnsNumber)
        endX = np.random.randint(0, columnsNumber)

        startY = np.random.randint(0, rowsNumber)
        endY = np.random.randint(0, rowsNumber)

        line_length = np.hypot(abs(startX - endX),abs(startY-endY))

        cv2.line(line, (startX,startY), (endX,endY), 255, 1)

        intersections = cv2.bitwise_and(imageOutput, line)
        crossCount = np.sum(intersections == 255)

        if(crossCount != 0):
            result[i] = line_length/crossCount
            
    granularity = np.mean(result)
    file.write("Calculated granularity for " + filename + " is: " + str(granularity) + "\n\n")

#Główna część programu

path = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(path,"source")
output_path = os.path.join(path,"output")

if not os.path.exists(source_path):
    print("Source directory does not exist.")
    input("Press Enter to Exit...")
    exit()
    
if not os.path.exists(output_path):
        os.makedirs(output_path)

filepaths = glob.glob(source_path + "/*")
file = open((output_path + "/results.txt"), 'w')

for filepath in filepaths:
     edge_detection(filepath)

file.close()

