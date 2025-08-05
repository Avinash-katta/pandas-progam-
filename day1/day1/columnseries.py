import pandas as pd
names=pd.Series(['apples','oranges','kiwi'])
df=names.to_frame(name='Name')

#add new column
df['price']=[50,30,80]
print(df)
