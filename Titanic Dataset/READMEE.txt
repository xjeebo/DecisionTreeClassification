~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--
Contents:

decision2.py - main program

functions.py - headers

variables.py - headers that contains all variables

Submission_Output_file.csv - My output, if you execute the program you will get an Output_File.csv

test_set.csv - reads from the dataset and then classifies whether to play outside or not

TitanicRecords_training_set.csv - used by the main program to train the program

TitanicVariables.PNG - Desciption of the variables, I took this dataset from Kaggle.
		       Since I hard coded everything, I decided to remove some of the variables to reduce the amount 
		       code. I still managed a pretty decent accuracy. 
~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--
To Execute Program:
python decision2.py

Expected Output:
Output_File.csv


~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--
Note: The difference between Test_dataset.csv and Training_dataset.csv 
is that Test_dataset.csv has a column removed; "Survived." The purpose of the 
Test_dataset.csv is to fill out the "Survived" column by implementing the 
Decision Tree classification algorithm.
