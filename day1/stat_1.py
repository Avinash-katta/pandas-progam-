"""Code to show the computation of statistics and access Series attributes 
100 150 200 300 250 .
print original data , which is serialized statistics:
mean ,sum,max,min,attributes
 Index=['a'......'e']
val=[100.0,.........250.0]"""
import pandas as p
print("Enter 5 random numbers ,space seperated:")
num=input().strip().split()
num=[float(n) for n in num]
try:
    if len(num)!=5:
        raise ValueError("please enter 5 num only ")
    s=p.Series(num,index=['a','b','c','d','e'])
    print("\n Original Series")
    print(s)
    #STATISTICS
    print("\n  Stats")
    print(f"Mean:{s.mean()}")
    print(f"sum:{s.sum()}")
    print(f"Max:{s.max()}")
    print(f"Min:{s.min()}")
    #Attributes
    print("\n Attributes")

    print(f" Index: {s.index.tolist()}")
    print(f" Values: {s.values.tolist()}")
    print(f" DataType: {s.dtype}")
except ValueError as e:
    print(f"Error:{e}")