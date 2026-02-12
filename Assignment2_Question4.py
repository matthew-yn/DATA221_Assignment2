#Imports pandas package as pd.
import pandas as pd

#Reads csv into a DataFrame.
df = pd.read_csv("student.csv")

#Creates a new DataFrame with the filtered data.
filtered_df = df[
    (df["studytime"] >= 3) &
    (df["internet"] == 1) &
    (df["absences"] <= 5)
]

#Converts filtered DataFrame into a csv.
filtered_df.to_csv("high_engagement.csv", index=False)

#Prints number of students saved into filtered DataFrame.
print("Students saved:", len(filtered_df))
#Prints average grade of students saved.
print("Average grade:", filtered_df["grade"].mean())