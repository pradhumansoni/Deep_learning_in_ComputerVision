import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def histequal():
    root = os.getcwd()
    imgPath = os.path.join(root , "4.image_filter\\cute.jpg")
    img = cv.imread(imgPath , cv.IMREAD_GRAYSCALE)

    plt.imshow(img , cmap='gray')
    hist = cv.calcHist(img , [0] , None , [256] , [0,256])
    cdf = np.cumsum(hist)
    cdfNorm = cdf * float(hist.max()) / float(cdf.max())
    plt.figure()
    plt.plot(hist , label='hist')
    plt.plot(cdfNorm , label = 'cdfNorm')
    plt.legend()
    plt.show()

    # Let us now use histogram equalizer
    equImg = cv.equalizeHist(img)
    plt.imshow(equImg , cmap='gray')
    equHist = cv.calcHist(equImg , [0] , None , [256] , [0,256])
    equcdf = np.cumsum(equHist)
    equcdfNorm = equcdf * float(hist.max()) / float(cdf.max())
    plt.figure()
    plt.plot(hist , label='hist')
    plt.plot(equcdfNorm , label = 'EqucdfNorm')
    plt.legend()


    plt.show()




if __name__ == "__main__":
    histequal()