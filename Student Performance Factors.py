import pandas as pd
import matplotlib.pyplot as plt

# Loading the spreadsheet
file_path = 'StudentPerformanceFactors.xlsx'  # Update with the correct path if necessary
excel_data = pd.ExcelFile(file_path)
df = excel_data.parse(excel_data.sheet_names[0])  # Load the first sheet

# Displaying basic information about the dataset
print("Initial dataset info:")
print(df.info())

# Removing rows with any missing values
df.dropna(inplace=True)

# Ensuring that numeric columns are of the correct type
# Adjusting based on your dataset columns
numeric_columns = ['Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores', 'Tutoring_Sessions', 
                   'Physical_Activity', 'Exam_Score']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Droping irrelevant columns if necessary (customized as needed)
# df.drop(columns=['Unnecessary_Column_Name'], inplace=True)

# Displayig cleaned dataset info
print("\nDataset info after cleaning:")
print(df.info())

# Saving the cleaned data to a new file
df.to_excel('Cleaned_StudentPerformanceFactors.xlsx', index=False)
print("Cleaned dataset saved as 'Cleaned_StudentPerformanceFactors.xlsx'")

# Visualization

# Bar Chart: Average Exam Score by Attendance Level
attendance_bins = [0, 50, 75, 100]  # Define attendance levels
attendance_labels = ['Low (0-50%)', 'Medium (50-75%)', 'High (75-100%)']
df['Attendance_Level'] = pd.cut(df['Attendance'], bins=attendance_bins, labels=attendance_labels)
avg_exam_score_by_attendance = df.groupby('Attendance_Level')['Exam_Score'].mean()

plt.figure(figsize=(8, 5))
avg_exam_score_by_attendance.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Exam Score by Attendance Level')
plt.xlabel('Attendance Level')
plt.ylabel('Average Exam Score')
plt.xticks(rotation=45)