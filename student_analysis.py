import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student.csv")
print(df.info())
df = df.drop(columns=["assignments_submitted"])
df["total_marks"] = (
    df["quiz1_marks"] +
    df["quiz2_marks"] +
    df["quiz3_marks"] +
    df["midterm_marks"] +
    df["final_marks"]
)
df["attendance_percent"] = (df["lectures_attended"] / df["total_lectures"]) * 100
df["lab_attendance_percent"] = (df["labs_attended"] / df["total_lab_sessions"]) * 100

print("\nAverage Total Marks:", df["total_marks"].mean())

gender_perf = df.groupby("gender")["total_marks"].mean()
print("\nGender-wise Performance:\n", gender_perf)

top_students = df.sort_values("total_marks", ascending=False).head(5)
print("\nTop 5 Students:\n", top_students[["name", "total_marks"]])

attendance_marks = df[["attendance_percent", "total_marks"]]
print("\nAttendance vs Marks:\n", attendance_marks.head())

gpa_marks = df[["previous_gpa", "total_marks"]]
print("\nGPA vs Marks:\n", gpa_marks.head())

# Gender vs Marks
gender_perf.plot(kind="bar")
plt.title("Gender vs Average Marks")
plt.xlabel("Gender")
plt.ylabel("Marks")
plt.show()

# Attendance vs Marks (Scatter)
plt.scatter(df["attendance_percent"], df["total_marks"])
plt.title("Attendance vs Total Marks")
plt.xlabel("Attendance %")
plt.ylabel("Marks")
plt.show()

# GPA vs Marks (Scatter)
plt.scatter(df["previous_gpa"], df["total_marks"])
plt.title("Previous GPA vs Total Marks")
plt.xlabel("GPA")
plt.ylabel("Marks")
plt.show()