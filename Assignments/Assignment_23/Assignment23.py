import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay)

######################################################################
#   Step 1 : Load the dataset
######################################################################

df = pd.read_csv("student_performance_ml.csv")

print("Dataset gets loaded successfully...")
print(df.head())

######################################################################
#   Step 2 : Data Analysis (EDA)
######################################################################

print("Shape of Dataset : ",df.shape)
print("Columns Names : ",list(df.columns))

print("Missing values (Per Column) : ")
print(df.isnull().sum())

print("Class Distribution (FinalResult Count) : ")
print(df["FinalResult"].value_counts())

print("Statistical report os dataset : ")
print(df.describe())

######################################################################
#   Step 3 : Decide Independent & Dependent variables
######################################################################

features_cols = ["StudyHours",
                 "Attendance",
                 "PreviousScore",
                 "AssignmentsCompleted",
                 "SleepHours"]

X = df[features_cols]
Y = df["FinalResult"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

######################################################################
#   Step 4 : Visualisation of dataset
######################################################################

plt.figure(figsize=(7,5))

plt.scatter(df['StudyHours'], df['PreviousScore'])
plt.title("StudyHours VS PreviousScore")

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.grid(True)
plt.show()

######################################################################
#   Step 5 : Split the Dataset for training & testing
######################################################################

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Data spliting activity done : ")

print("X - Independent : ",X.shape)
print("Y - Dependent : ",Y.shape)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)
print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

######################################################################
#   Step 6 : Build the model
######################################################################

model = DecisionTreeClassifier(max_depth=5,random_state=42)

print("Model successfully created : ",model)

######################################################################
#   Step 7 : Train the model
######################################################################

model.fit(X_train,Y_train)

print("Model training completed")\

######################################################################
#   Step 8 : Test the model
######################################################################

Y_pred = model.predict(X_test)

print("Model Testing complete")

print(Y_pred.shape)

print("Expected answers : ")
print(Y_test)

print("Predicted answers : ")
print(Y_pred)

######################################################################
#   Step 9 : Test the model Performance
######################################################################

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is : ",accuracy*100)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion matrix : ")
print(cm)

print("Classification Report : ")
print(classification_report(Y_test,Y_pred))

######################################################################
#   Step 10 : Plot confusion matrix
######################################################################

data = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
data.plot()

plt.title("Confusion Matrix of student_performance dataset")
plt.show()