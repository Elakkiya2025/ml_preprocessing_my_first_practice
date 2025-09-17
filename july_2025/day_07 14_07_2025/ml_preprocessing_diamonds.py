import pandas as pd
df=pd.read_csv("diamonds.csv")
print(df)
coloum_types = df.dtypes
print(coloum_types)

# Below code read for first 10 rows
df= pd.read_csv("diamonds.csv")
print(df.head(10))

# Below codes read for last 20 rows only
df= pd.read_csv("diamonds.csv")
print(df.tail(20))
pd.set_option("display.max_rows",None)
"""below code is- if we using only isnull means null value will be shown for each coloumn"""
# finding_null_value= df.isnull().sum()
# print(finding_null_value)

"""shows summation of all null values"""
# finding_null_value=df.isnull().sum().sum()
# print(finding_null_value)

# finding_null_value = df.isna().sum()
# print(finding_null_value)

# finding_null_value=df.isna().sum().sum()
# print(finding_null_value)


"""Below code is for Filling of na datas"""
# df['carat']=df["carat"].fillna("Elak")
# print(df)

"""Below code is for Filling of more than one na datas"""
# df[['carat','cut']] = df[['carat','cut']].fillna("Elak")
# print(df)

"""Below code is for Filling of entire na datas"""
# df.fillna("Yaswanth Sai", inplace=True)
# print(df)

"""using mean of specific column to fill the empty spaces in entire na datas"""
# df.fillna(df['carat'].mean(), inplace=True)
# print(df)

"""rounding of carat column"""
# df['carat']=df['carat'].round()
# print(df)
"""rounding of carat column in 2 decimal places"""
# df['carat']=df['carat'].round(2)
# print(df)

"""to change the datatype from integer to float"""
# df['Unnamed: 0'] = df['Unnamed: 0'].astype(float)
# print(df)

"""Filling an empty spaces with using sklearn"""
from sklearn.impute import SimpleImputer

# si=SimpleImputer()
# df["carat"]=si.fit_transform(df[["carat"]])
# print(df)

"""filling an empty spaces with most frequent """
# si= SimpleImputer(strategy="most_frequent")
# df['carat']= si.fit_transform(df[['carat']])
# print(df)
"""fliing constant value in startegy """
# si=SimpleImputer(strategy="constant", fill_value=200)
# df['carat']=si.fit_transform(df[['carat']])
# print(df)
"""below code for drop the na values in the file"""
# df.dropna(inplace=True)
# print(df)

"""reset the index number after dropped the na value"""
# df.dropna(inplace=True)
# df.reset_index(inplace=True)
# print(df)

"""finding Duplicates"""
# finding_duplicate = df[df.duplicated()]
# print(finding_duplicate)
"""dropping the duplicates"""
# df.drop_duplicates(inplace=True)
# print(df)
"""dropping the duplicates and keep last duplicated"""
df.drop_duplicates(keep="last", inplace=True)
print(df)