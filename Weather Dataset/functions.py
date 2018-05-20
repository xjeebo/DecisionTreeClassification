import pandas as pd
import numpy as np
from variables import *
from sklearn import tree

def train():
    file = pd.read_csv("Training_Dataset.csv")
    return file["outlook"],file["temperature"],file["humidity"],file["windy"],file["play"]
def test():
    file = pd.read_csv("Test_Dataset.csv")
    return file["outlook"],file["temperature"],file["humidity"],file["windy"]   

# represent different parameters as integer values
def make_conversions(outlook,temperaturelevel,humiditylevel,windyornot):
    for i in range(0,len(outlook)):
        if outlook[i] == "sunny":
            outlook_conv.append(1)
        if outlook[i] == "overcast":
            outlook_conv.append(2)
        if outlook[i] == "rainy":
            outlook_conv.append(3)

    for i in range(0,len(temperaturelevel)):
        if temperaturelevel[i] == "hot":
            temperature_conv.append(1)
        if temperaturelevel[i] == "mild":
            temperature_conv.append(2)
        if temperaturelevel[i] == "cool":
            temperature_conv.append(3)

    for i in range(0,len(humiditylevel)):
        if humiditylevel[i] == "high":
            humidity_conv.append(1)
        if humiditylevel[i] == "normal":
            humidity_conv.append(2)

    for i in range(0,len(windyornot)):
        if windyornot[i] == True:
            windy_conv.append(1)
        if windyornot[i] == False:
            windy_conv.append(2)
            
def output_data(outlook,temperaturelevel,humiditylevel,windyornot,clf,playornot):
    accuracy = 0
    fo = open("Output_File.csv", "w") # output file based on decision tree
    fo.write("outlook,temperature,humidity,windy,Decision Made By Decision Tree\n")
    for i in range(0,len(outlook)):
        fo.write(str(outlook[i])+',')
        fo.write(str(temperaturelevel[i])+',')
        fo.write(str(humiditylevel[i])+',')
        fo.write(str(windyornot[i])+',')
        prediction = (clf.predict([x[i]]))
        fo.write(str(prediction)+"\n")

        # obtain the accuracy of the decision tree by comparing data from the training set
        # to what was classified by the decision tree
        if prediction == 'yes' and playornot[i] == "yes":
            accuracy += 1
        elif prediction == 'no' and playornot[i] == "no":
            accuracy += 1
    print("Decision Tree Accuracy: "+str(100*(accuracy/len(outlook)))+'%')




        