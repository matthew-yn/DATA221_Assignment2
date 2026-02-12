#Imports pandas package as pd.
import pandas as pd

#Converts students.csv to DataFrame.
df = pd.read_csv("student.csv")
#Creates a list to store grade bands.
bands = []

#Loops through each grade in CSV.
for grades in df["grade"]:
    #Low band if grades are less than or equal to 9.
    if grades <= 9:
        bands.append("Low")
    #Medium band if grades are greater than 9 and less than or equal to 14.
    elif grades <= 14:
        bands.append("Medium")
    #High band if grades are greater than 14.
    else:
        bands.append("High")

#Creates new column in DataFrame.
df["grade_band"] = bands
#Groups data by grade_band.
grouped = df.groupby("grade_band")

#Creates summary table and computes required calculations.
summary = grouped.agg({
    "grade": "count",
    "absences": "mean",
    "internet": "mean"
})

#Converts internet average into percentage.
summary["internet"] = summary["internet"] * 100

#Renames columns in summary DataFrame after calculations.
summary = summary.rename(columns = {
    "grade": "num_students",
    "absences": "avg_absences",
    "internet": "internet_percentage"
})

#Converts DataFrame into CSV.
summary.to_csv("student_bands.csv")