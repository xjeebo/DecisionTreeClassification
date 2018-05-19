import pandas as pd
import numpy as np
from variables import *
from sklearn import tree

def train():
    file = pd.read_csv("TitanicRecords_training_set.csv")
    return file["Name"],file["Pclass"],file["Sex"],file["SibSp"],file["Parch"],file["Embarked"],file["Survived"]

def test():
    file = pd.read_csv("test_set.csv")
    return file["Name"],file["Pclass"],file["Sex"],file["SibSp"],file["Parch"],file["Embarked"]

def make_conversions(Pclass,Sex,SibSp,Parch,Embarked):
    for i in range(0,len(Pclass)):
        if Pclass[i] == 1:
            pclass_conv.append(1)
        elif Pclass[i] == 2:
            pclass_conv.append(2)
        elif Pclass[i] == 3:
            pclass_conv.append(3)

    for i in range(0,len(Sex)):
        if Sex[i] == "male":
            sex_conv.append(1)
        elif Sex[i] == "female":
            sex_conv.append(2)
            
    for i in range(0,len(SibSp)):
        if SibSp[i] == 0:
            sibsp_conv.append(0)
        else:
            sibsp_conv.append(1)
        
    for i in range(0,len(Parch)):
        if Parch[i] == 0:
            parch_conv.append(0)
        else: 
            parch_conv.append(1)

    for i in range(0, len(Embarked)):
            if Embarked[i] == 'C':
                embarked_conv.append(1)
            elif Embarked[i] == 'Q':
                embarked_conv.append(2)
            else:
                embarked_conv.append(3)

def output_data(name,Pclass,Sex,SibSp,Parch,Survived,Embarked,clf):
    accuracy = 0
    fo = open("Output_File.csv", "w") # output file based on Naive Bayes Classification
    fo.write("Name,\t,Pclass,Sex,SibSp,Parch,Embarked,Survived Classification Made By Decision Tree\n")
    for i in range(0,len(name)):
        fo.write(str(name[i])+',')
        fo.write(str(Pclass[i])+',')
        fo.write(str(Sex[i])+',')
        fo.write(str(SibSp[i])+',')
        fo.write(str(Parch[i])+',')
        fo.write(str(Embarked[i])+',')
        prediction = (clf.predict([x[i]]))
        fo.write(str(prediction)+"\n")

        if prediction == 1 and Survived[i] == 1:
            accuracy += 1
        elif prediction == 0 and Survived[i] == 0:
            accuracy += 1
    print("Decision Tree Accuracy: "+str(100*(accuracy/len(name)))+'%')


