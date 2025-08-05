import pandas as pd

'''
1. series (1-D Array)
2. Dataframes (2-D Array)/ labeling will be on rows and column
operations:
1. reading / writing of data (csv/json/xls)
2. inserting of data
3. selecting of data
4. data manipulation
5.grouping andagregation
6.merging / joining
7.sorting

syntax: DataFrame (data)
df.head(n) first n rows
df.tail(n) last n rows
df.info() summary -df
df.describe()- stat summary
df.shape()- tuple rows columns
df.dtypes()-data type (column)
df.column()- column name
'''

# print("Enter 3 names seperated with space: ")
# names=input().strip().split()
# print("Enter 3 index labels: ")
# indices=input().strip().split()
# try:
#     if len(names)!=3 or len(indices)!=3:
#         raise ValueError("Please provide exact names with indices")
#     series=pd.Series(data=names, index=indices)
#     print("Created a new series: ")
#     print(series)
# except ValueError as e:
#     print(f"Error:{e}")


# print("Enter 4 random numbers with space seperated: ")
# numbers=input().strip().split()
# numbers=[float(num) for num in numbers]
# try:
#     if len(numbers)!=4:
#         raise ValueError("Please provide exact 4 numbers: ")
#     total_data=pd.Series(numbers)
#     print(total_data)
    
#     filtered=total_data[total_data>10]
# except ValueError as e:
#     print(f"Error:{e}")



# print("Enter 5 strings, space seperated:")
# strings=input().strip().split()
# print("Enter substring:")
# substring=input().strip()
# try:
#     if len(strings) != 5:
#         raise ValueError("Please provide 5 strings only:")
#     series= pd.Series (strings)
#     print("\n Original Series: ")
#     print(series)
#     filtered_series= series[series.str.lower().str.contains(substring.lower(),na=False)]
#     print(f"strings containing '{substring}'(case-sensitive):")
#     print(filtered_series if not filtered_series.empty else 'No match found .')
# except ValueError as e:
#     print(f"Error:{e}")
    

# import numpy as np
# series=pd.Series([10,np.nan,30,np.nan,50],index=['a','b','c','d','e'])
# print("\n Original Series: ")
# print(series)
# print("\n missing values: ")
# print(series.isna())
# filled_series=series.fillna(0)
# print(filled_series)
# dropped_series=series.dropna()
# print(dropped_series)

# import pandas as pd
# print("Enter 5 random numbers, space seperated: ")
# numbers= input().strip().split()
# numbers=[float(num) for num in numbers]
# try:
#     if len(numbers) != 5:
#         raise ValueError("Please enter 5 numbers only!!!")
#     series= pd.Series(numbers, index=['a', 'b','c','d','e'])
#     print("\n Original series:")
#     print(series)
# # Statistics
#     print("\n Statstics:")
#     print(f"Mean:{series.mean()}")
#     print(f"Sum:{series.sum()}")
#     print(f"Max:{series.max()}")
#     print(f"Min:{series.min()}")
# #Attributes
#     print("\n Attributes")
#     print(f"index: {series.index.tolist()}")
#     print(f"values: {series.values.tolist()}")
#     print(f"s.dtype")
    
    
# except ValueError as e:
#     print(f"Error:{e}")
    
    
# import pandas as pd
# print("enter 4 numbers, space seperated: ")
# numbers= input().strip().split()
# numbers=[float(num) for num in numbers]
# try:
#     if len(numbers)!= 4:
#         raise ValueError("Give 4 numbers only!!!")
#     series= pd.Serles (numbers, index=['a', 'b', 'c', 'd'])
#     print("\n Original Series: ")
#     print(series)

#     doubled=series*2
#     print("\n series after doubling series")
#     print(doubled)

#     added =series+100
#     print("\n series fter addig 100")
#     print(added)

# except ValueError as e:
#     print(f"Error {e}")


# import pandas as pd
# data= {'Name': ['Mark', 'Steve', 'Jenny'],'Age': [22,21,22],'Branch': ['EEE', 'CSE', 'Mech']}
# dframe=pd.DataFrame(data)
# print(dframe)



# import pandas as pd
# n=int(input("Enter number of profiles:"))
# names=[]
# ages=[]
# branches=[]
# for i in range(n):
#     print(f"----Ener {i+1}----")
#     name=input("Enter Name: ")
#     age=input("Enter Age: ")
#     branch=input("Enter Branch: ")
#     names.append(name)
#     ages.append(age)
#     branches.append(branch)
# data={'Name':names, 'Age':ages, 'Branch':branches}
# dframe=pd.DataFrame(data)
# print(dframe)


# import pandas as p
# import numpy as n
# d={
#     'Patient_id':['P001','P002','P003','P004','P005','P006']
#     ,'Name':['Vijay','Raiser','Devara','Mushtq','Avinash',None]
#     ,'Age':[34,30,None,60,25,50],'Department':['Covid','TB','Cancer','Cardiology','Accident','ICU']
#     ,'Admission-Date':['2025-01-15','2024-02-24','2025-03-28','2026-03-25','30-7-2023','']
#     ,'Bill':[7000.78,7590,9000,8900,8700,None]
#   }
# df=p.DataFrame(d)
# df.to_csv('hospital_data.csv',index=False)
# print("Successfull creation")


# import pandas as pd
# try:
#   df =pd.read_csv('hospital_data.csv')
#   print("\n Hospital DataFrame: ")
#   print(df)
#   print("\n DataFrame INFO: ")
#   print(df.info())
#   print("\n Summary Statistics: ")
#   print(df.describe())
# except FileNotFoundError:
#   print("Error: 'hospital_data.csv' not found.")


import pandas as pd
try:
  df=pd.read_csv('hospital_data.csv')
  print("\n Original hospital DataFrame")
  print(df) 
# check missing values.
  print("\n Missing Values:")
  print(df.isna())
#filling name by unknown, value
  df_filled=df.copy()
  df_filled['Name']= df_filled['Name'].fillna('Unknown')
  df_filled['Age']= df_filled['Age'].fillna(df_filled['Age'].mean())
  df_filled['Bill']= df_filled['Bill'].fillna(0)
  print("\n dataframe after filling by default: ")
  print(df_filled)
except FileNotFoundError:
  print("Error: 'hospital_data.csv' not found")
  
  
