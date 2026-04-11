import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset from CSV file
df = pd.read_csv("student_performance_ml.csv")

# Display first 5 records
print("First 5 records : \n", df.head())

# Display last 5 records
print("\nLast 5 records : \n", df.tail())

# Display shape (rows, columns)
print("\nShape of dataset : \n", df.shape)

# Display column names
print("\nColumn names : ", df.columns.tolist())
 
# Display data types of each column
print("\nData types: \n", df.dtypes)

# Total number of students (rows)
print("Total students : ",len(df))

# Count number of passed students (FinalResult = 1)
pass_count = (df['FinalResult'] == 1).sum()
print("Passed students : ",pass_count)

# Count number of failed students (FinalResult = 0)
fail_count = (df['FinalResult'] == 0).sum()
print("Failed students : ",fail_count)

print("Average StudyHours : ",df['StudyHours'].mean())
print("Average Attendance : ",df['Attendance'].mean())
print("Maximum PreviousScore : ",df['PreviousScore'].max())
print("Maximum SleepHours : ",df['SleepHours'].max())

# Count distribution of FinalResult (Pass/Fail)
result_counts = df['FinalResult'].value_counts()
print("\nDistribution : \n", result_counts)

# Calculate percentage distribution
percentage = df['FinalResult'].value_counts(normalize=True) * 100
print("\nPercentage : \n",percentage)

# Check whether dataset is balanced or not
if abs(percentage[1] - percentage[0]) < 10:
    print("Dataset is Balanced")
else:
    print("Dataset is NOT Balanced")   

# Histogram for Study Hours distribution
plt.hist(df['StudyHours'])
plt.title("StudyHours Distribution")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()     

colors = df['FinalResult'].map({1:'green', 0: 'red'})

# Scatter plot between StudyHours and PreviousScore
plt.scatter(df['StudyHours'],
            df['PreviousScore'], c=colors)
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.title("StudyHours vs PreviousScore")
plt.show()

# Boxplot for Attendance
plt.boxplot(df['Attendance'])
plt.title("Attendance Boxplot")
plt.show()

# Seaborn boxplot for AssignmentsCompleted vs FinalResult
sns.boxplot(x='FinalResult',
            y='AssignmentsCompleted', data=df)

plt.title("AssignmentsCompleted vs FinalResult")
plt.show()