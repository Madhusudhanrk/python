import pandas as pd
from pandas.core.frame import DataFrame

#counting no of times every letter present in phrase
phrase = "Madhusudhan"
print(pd.Series(list(phrase)).value_counts())

#dataframe
print("dataFrame from excel\n")

df = pd.read_excel('bio.xlsx')
print(df)

print("dataFrame from dict\n")

bio =[{
    'name':'madhu',
    'age':23,
    'gender':'male'
}]
df2= DataFrame(bio)
print(df2)

print("dataFrame from appended\n")

print(df2.append(df))


print("dataFrame from concat\n")

print(pd.concat([df,df2]))


print("dataFrame from join\n")

print(df.join(df2))




