'code elobrates how to filter string data in series basedo insensitivity)'''

import pandas as pd
print("Enter 5 strings, space seperated: ")
strings= input().strip().split()
print("Enter substring:")
substring= input().strip()
try:
    if len(strings)!= 5:
        raise ValueError("please provide 5 strings only:")
    series=pd.Series(strings)
    print("\n original Series")
    print(series)
    filtered_series=series[series.str.lower().str.contains(substring.lower(),na=False)]
    print(f" strings contains '{substring} '(case-intensitive):")
    print(filtered_series if not filtered_series.empty else "No match found .")
    
except ValueError as e:
    print(f"Error: {e}")
