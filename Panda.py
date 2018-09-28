import pandas as pd
fname = "C:\Python Test Files\Weather_Data.csv"
df = pd.read_csv(fname)
print(df)
###
print(df["Coupon (%)"].max())
print(df["As Of Date"][df["T Bill"] == "T Bill"])
print(df.shape)
df = pd.read_excel("C:\Python Test Files\Weather.xlsx", "Sheet1")
print(df)


df = pd.read_csv("C:\Python Test Files\SOMA_HOLDINGS_Replace.csv")
print(df)

df2y = pd.read_csv("C:\Python Test Files\Y2TreasuryYields.csv")
print(df2y)
print(type(df2y.DATE[0]))
###