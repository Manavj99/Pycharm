import pandas as pd

# ages =pd.Series([18,21,25])
# print(ages)

# data = {
#     "name": ["Alice", "Bob", "Charlie"],
#     "age": [20, 22, 19],
#     "score": [85, 90, 88]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.tail())


# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.values)
# print(df.head(2))
# print(df.tail(2))
# print(df.sample(2))
# print(df.sort_values(by="age"))
# print(df.sort_values(by="age", ascending=False))

df = pd.read_csv("C:/Users/Manav/Downloads/sales_orders_dataset.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# df.dropna(inplace=True)
# print(df)
# df.fillna(0, inplace=True)
# print(df)
#df.info()
# df["customer_id"] = df["customer_id"].astype("string")
# print(df.info())

# df["customer_id"] = df["customer_id"].astype("int64")
# print(df.info())

# print(df.drop_duplicates(inplace=True))

# print(df[df["unit_price"] > 400])

# print(df[["customer_id", "order_id"]])

# print(df.sort_values(by="unit_price", ascending=False))

#print(df.groupby("customer_id")["total_amount"].sum())

# pd.merge(df, df, on="customer_id", how="left")

#print(df.shape)

# print(len(df))

# print(df.iloc[9])

# df.to_csv("C:/Users/Manav/Downloads/sales_orders_dataset_copy.csv", index=False)

