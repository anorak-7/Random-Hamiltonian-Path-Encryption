import cv2
import numpy as np

#Bit plane decomposition
def decompositon(img):
    newImg = np.zeros((2 * img.shape[0], 2 * img.shape[1]))
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            newImg[row][col] = (img[row][col] >> 6) & 3 # (img[row][col] >> 6) & 00000011 
            newImg[row][col + img.shape[1]] = (img[row][col] >> 4) & 3 # (img[row][col] >> 4) & 00000011 
            newImg[row + img.shape[0]][col] = (img[row][col] >> 2) & 3 # (img[row][col] >> 2) & 00000011 
            newImg[row + img.shape[0]][col + img.shape[1]] = (img[row][col]) & 3 # (img[row][col]) & 00000011 

    return newImg

def compose(img):
    newImg = np.zeros((int(img.shape[0] / 2), int(img.shape[1] / 2)))
    for row in range( int(img.shape[0] / 2)):
        for col in range(int (img.shape[1] / 2)):
            x = int(img[row][col]) << 6
            y = int(img[row][col + int(img.shape[1] / 2) ]) << 4
            z = int(img[row + int(img.shape[0] / 2)][col]) << 2
            u = int(img[row + int(img.shape[0] / 2)][col + int(img.shape[1] / 2)])
            newImg[row][col] =  x + y + z + u 

    return newImg