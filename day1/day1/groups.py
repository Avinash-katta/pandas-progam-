import pandas as pd
try:
    df=pd.read_csv('hospital_data.csv')
    print("\n Original Hospital DataFrame")
    print(df) 
# grouping by department
    grouped=df.groupby('Department')['Bill'].mean()
    print("\n Average Medical Cost by Department ")
    print(grouped)
except FileNotFoundError:
    print("Error: 'Hospital_data.csv' not found.")