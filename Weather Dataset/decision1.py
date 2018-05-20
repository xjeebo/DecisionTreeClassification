from sklearn import tree
from variables import *
from functions import make_conversions,train,output_data,test

# train the program
outlook,temperaturelevel,humiditylevel,windyornot,playornot = train()
make_conversions(outlook,temperaturelevel,humiditylevel,windyornot)

# test the program, this recieved the inputs from the test set
outlook,temperaturelevel,humiditylevel,windyornot = test()
make_conversions(outlook,temperaturelevel,humiditylevel,windyornot)

# fill x with all possible parameters for each day
for j in range(0,14):        
    z.append(outlook_conv[j])
    z.append(temperature_conv[j])
    z.append(humidity_conv[j])
    z.append(windy_conv[j])
    x.append(z)
    z = []

# apply to sklearns function
y = playornot
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# output a csv to compare results to the original training dataset
output_data(outlook,temperaturelevel,humiditylevel,windyornot,clf,playornot)