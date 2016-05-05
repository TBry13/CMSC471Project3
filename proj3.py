'''
* To run type "python proj3.py"
* Here is my project 3. No it does not work fully. I had tried to ask around in class to see what other people did and I could not replicate that.
* To run the program you need the data sitting in a learn folder and a predict folder, numbered sequentially(1.jpg, 2.jpg,.... 381.jpg). The learn and
* predict folders sit inside of a data folder that is on the same level as the python code. It would run on its own and print out the prediction of the 
* 20 jpgs sitting in the predict folder in one array.
* 100% correct predicion would be ["Hat", "Hash", "Hat", "Dollar", "Heart", "Hash", "Smile", "Heart", "Smile", "Hash", "Heart", "Dollar", "Hat", "Hash",
* "Dollar", "Heart", "Dollar", "Smile", "Hat", "Hash"]
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from sklearn import datasets
from sklearn import svm

def main():
    clf = svm.SVC(gamma=0.001, C=100)
    i = 1
    learnMax = 381
    predictMax = 20
    learnX = []
    learnY = []
    while (i <= learnMax):
        learnX.append(mpimg.imread("data\\learn\\" + str(i) + ".jpg"))
        #print(learnX[i-1].shape)
        if i < 81:
            learnY.append("Smile")
        if i >= 81 and i < 149:
            learnY.append("Hat")
        if i >= 149 and i < 221:
            learnY.append("Hash")
        if i >= 221 and i < 299:
            learnY.append("Heart")
        if i >= 299:
            learnY.append("Dollar")

        i = i + 1
    print("It does not work correctly unfortunately. I was never able to get the SVM working for either Sklearn or OpenCV. I can get the images processed into arrays, but then trying to get them into the SVM caused me a whole bunch of trouble.")
    print("I have the rest of the code written just commented out because I just gives me errors.")
    '''
    clf.fit(learnX, learnY)
    
    predictX = []
    while (i <= predictMax):
        predictX.append(mpimg.imread("data\\predict\\" + str(i) + ".jpg"))
        #print(predictX[i-1].shape)
        i = i + 1

    predictY = clf.predict(predictX)
    print(predictY)
    answer = ["Hat", "Hash", "Hat", "Dollar", "Heart", "Hash", "Smile", "Heart", "Smile", "Hash", "Heart", "Dollar", "Hat", "Hash", "Dollar", "Heart", "Dollar", "Smile", "Hat", "Hash"]
    print(answer)
    '''

main()





