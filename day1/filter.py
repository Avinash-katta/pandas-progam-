
# code elobrates how to filter numerical data in series basedon conditiion (e.g:
# values greater than a threshold"

import pandas as pd
print("Enter 4 random number, space seperated")
numbers=input().strip().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers)!= 4:
        raise ValueError("please provide exactly 4 numbers:")
    total_data=pd.Series(numbers)
    print(total_data)

    filtered=total_data[total_data>10]

    print("values >10")
    print(filtered)
except ValueError as e:
    print(f"Error {e}")
