import pandas as pd

df = pd.read_csv()

#Assortment - describes an assortment level: a = basic, b = extra, c = extended
df['Assortment'] = df['Assortment'].replace({"a": 1, "b": 2, "c": 3})