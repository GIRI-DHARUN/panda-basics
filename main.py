import pandas as pd

# print("Day 1 of learning")

data={
"day":["Mon","Tue","Wed","Thu","Fri"],
    "study_hours": [2,3,1.5,4,2.5]
}

df=pd.DataFrame(data)

print(df)
print("\nAverage study hours:",df["study_hours"].mean())
