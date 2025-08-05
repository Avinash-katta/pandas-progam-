import pandas as pd
try:
    df=pd.read_csv('hospital_data.csv')
    print('\n Orginal Hospital dataframe')
    print(df)

#add discount_cost column (10% discount)
    df['Discount']=df['Bill']*0.9

#sorting bill
    sorted_df=df.sort_values('Bill',ascending=False)
    print('\n Sorted by medical Bills (descending order)')
    print(sorted_df)
except FileNotFoundError:
    print("Error : Hospital_data.csv not found")