#Imports pandas package as pd.
import pandas as pd

#Reads csv into a DataFrame.
df = pd.read_csv("crime.csv")

#Creates a list to store crime levels.
risk_list = []

#Loops through each value in ViolentCrimesPerPop.
for value in df["ViolentCrimesPerPop"]:
    #If values is larger than or equal to 0.50 crime level is high.
    if value >= 0.50:
        risk_list.append("HighCrime")
    #Set everything else to low crime level.
    else:
        risk_list.append("LowCrime")

#Adds new column to DataFrame called risk.
df["risk"] = risk_list

#Groups data by risk column and calculates the average unemployment.
result = df.groupby("risk")["PctUnemployed"].mean()

#Prints average unemployment for each group back to user.
print("HighCrime average unemployment:", result["HighCrime"])
print("LowCrime average unemployment:", result["LowCrime"])