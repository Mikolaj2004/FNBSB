import cv2
import numpy as np

#Funkcja oblicza ziarnistość na podstawie zdjęć z zastosowanym algorytmem Canny

def count(imageOutput, iterations = 200):
    result = [0 for _ in range(iterations)]
    for i in range(iterations):
        

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
         
    granularity = round((np.mean(result)/27.5),1)
    return granularity