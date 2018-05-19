from sklearn import tree
from variables import *
from functions import train,make_conversions,output_data,test

# train the program 
name,Pclass,Sex,SibSp,Parch,Embarked,Survived = train()
make_conversions(Pclass,Sex,SibSp,Parch,Embarked)

# test the program, this recieved the inputs from the test set
name,Pclass,Sex,SibSp,Parch,Embarked = test()
make_conversions(Pclass,Sex,SibSp,Parch,Embarked)

# fill x with all possible parameters for each person
for i in range(0,len(name)):
    z.append(pclass_conv[i])
    z.append(sex_conv[i])
    z.append(sibsp_conv[i])
    z.append(parch_conv[i])
    z.append(embarked_conv[i])
    x.append(z)
    z = []

# apply to sklearns function
y = Survived
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# output a csv to compare results to the original training dataset
output_data(name,Pclass,Sex,SibSp,Parch,Survived,Embarked,clf)




