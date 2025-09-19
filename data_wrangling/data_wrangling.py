import pandas as pd
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder


df= pd.read_csv("IPL2025Batters.csv")
print(df)

columns= df.columns
print(df)
print(df.dtypes)

object_columns=[]
for col in columns:
    if df[col].dtype == "O":
        object_columns.append(col)
print(object_columns)
"""conversion catagorical data into numerical data"""
team_categories_list = df["Team"].unique()
print(team_categories_list)

df["Team"]= df["Team"].map({'GT':0,'RCB':4,'LSG':5,'PBKS':6, 'RR':7 ,'DC':8, 'SRH':9, 'MI':10, 'KKR':11, 'CSK':12})
print(df)

""""using sklearn for conversion"""
"""Label Encoder"""
from sklearn.preprocessing import LabelEncoder
label_encoder_object = LabelEncoder()
df["Team"] = label_encoder_object.fit_transform(df["Team"])
print(df)
unique_data_postconversion = df["Team"].unique()
print(unique_data_postconversion)

"""Ordinal Encoder"""
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder_object= OrdinalEncoder()
df["Player Name"] = ordinal_encoder_object.fit_transform(df[["Player Name"]])
print(df)

unique_post_data_conversion = df["Player Name"].unique()
print(unique_post_data_conversion)