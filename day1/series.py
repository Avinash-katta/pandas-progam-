import pandas as pd
print("Enter 3 names seperaed with space")
names=input().strip().split()
print("Enter 3 index labels")
indices=input().strip().split()
try:
    if len(names)!= 3 or len(indices)!= 3:
        raise ValueError("please provide exact names with indices")
    series=pd.Series(data=names,index=indices)
    print("Created a new series")
    print(series)             
except ValueError as e:
    print(f"Error:{e}")



