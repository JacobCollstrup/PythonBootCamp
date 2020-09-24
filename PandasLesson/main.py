import pandas as pd
import numpy as np

x = ["a", "b", "c", "d", "e"]
x2 = ["a", "b", "c", "d", "e"]
y = [1, 2, 3, 4, 5]
z = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}

a = pd.Series(y, x)
b = pd.Series(y, x2)

print(a)
print(b)
print(a + b)  # Adds the data together in the two series...NANs for indexes not shared between the two series.

print(a["c":])  # prints the elements from index "c" and to the end of the series.

A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = [9, 0, 1, 2]
D = [3, 4, 5, 6]
E = [7, 8, 9, 0]

df = pd.DataFrame([A, B, C, D, E], ["a", "b", "c", "d", "e"], ["w", "x", "y", "z"])  # Creates dataframe of lists.
#  The order of input is data, rows, columns.

print(df)
df["p"] = df["y"] + df["z"]
print(df)

df.drop("e")  # temporarily drops the row "e".
# df.drop("e", inplace=True)  # Permanently deletes the row "e".
df.drop("p", axis=1)  # Temporarily drops the column "p"
# df.drop("p", axis=1, inplace=True)  # Permanently drops the column "p"

print(df)

print(df["y"])  # Accesses column "y".
print(df.loc["a"])  # Accesses row "a".
print(df.iloc(1))  # Accesses the rows by index. Theses are *not* zero indexed. 1 is the first row!
print(df.loc["d", "y"])  # Accesses the data element in row "d", column "y".

print(df > 3)  # Boolean table showing true for values larger than 3, false otherwise.
print(df[df > 3])  # Table containing values larger than 3. NaNs for values smaller or equal to 3. Numbers comes out as floats.
print(df[df["w"] > 3])  # Table with the rows from column "w" that are larger than 3.

print(df[df["w"] > 3][["w", "x"]])  # Table with columns "w" and "x", where the rows are larger than 3, in column "w"
print(df[df["w"] > 3][["x", "z"]])  # Table with columns "x" and "z", where the rows are larger than 3, in column "w"

# print(df[(df["w"] > 3) and (df["z"] > 2)])  # Results in error, since 'and' and 'or' keywords can't be used directly.
                                              # Curved parenthesis around conditionals are for readability.

print(df[(df["w"] > 3) & (df["z"] > 2)])  # returns the table that satisfies both conditions, column "w" larger than 3
                                          # and column "z" larger than 2.

print(df[(df["w"] > 3) | (df["z"] > 2)]) # returns that table that satisfies one of the conditions, column "w" larger than 3
                                          # and column "z" larger than 2.

d = {"a": [1, 2, 3, 4, 5], "b": [6, 7, 8, 9, np.nan], "c": [0, 1, 2, np.nan, np.nan], "d": [3, 4, np.nan, np.nan, np.nan], "e": [5, np.nan, np.nan, np.nan, np.nan]}
print(d)

df = pd.DataFrame(d)  # Converts variable "d" into a dataframe. Notice camel-type capitals.
print(df)

print(df.dropna(axis=0))  # Drops all rows with a NaN in it.
print(df.dropna(axis=1))  # Drops all columns with a NaN in it.
print(df.dropna(thresh=3))  # Keeps all rows with 3 or more data points.
print(df.fillna(1))  # Replaces all NaN values with 1.
print(df["b"].fillna(value=df["b"].mean()))  # Replaces the NaN in column "b" with the average of column "b".
print(df["c"].fillna(value=df["b"].mean()))  # Replaces the NaNs in column "c" with the average of column "b".


# Analysing using group-by

p = {"item": ["apple", "apple", "orange", "orange", "guns", "guns"], "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
     "sales": [100, 80, 200, 100, 5, 10]}

df = pd.DataFrame(p)

print(df)

x = df.groupby("item")
print(x)
print(x.mean())

print(x.sum())
print(x.describe().transpose())

x1 = {"a": [1, 2, 3], "b": [5, 6, 7]}
y1 = {"c": [3, 4, 5], "d": [2, 3, 6]}

x = pd.DataFrame(x1, index=["p1", "p2", "p3"])
y = pd.DataFrame(y1, index=["p1", "p4", "p5"])

print(x)
print(y)
print("*************************************")
print(x.join(y))
print("*************************************")
print(x.join(y, how="right"))
print("*************************************")

# Concatenating

x1 = {"a": [1, 1, 1, 1, 1], "b": [1, 1, 1, 1, 1], "c": [1, 1, 1, 1, 1], "d": [1, 1, 1, 1, 1], "e": [1, 1, 1, 1, 1]}
x2 = {"e": [2, 2, 2, 2, 2], "f": [2, 2, 2, 2, 2], "g": [2, 2, 2, 2, 2], "h": [2, 2, 2, 2, 2], "i": [2, 2, 2, 2, 2]}
x3 = {"a": [3, 3, 3, 3, 3], "b": [3, 3, 3, 3, 3], "c": [3, 3, 3, 3, 3], "d": [3, 3, 3, 3, 3], "e": [3, 3, 3, 3, 3]}

df1 = pd.DataFrame(x1, index=[1, 2, 3, 4, 5])
df2 = pd.DataFrame(x2, index=[1, 2, 3, 4, 5])
df3 = pd.DataFrame(x3, index=[5, 6, 7, 8, 9])

print(pd.concat([df1, df2, df3]))
print("*************************************")

# Merging

df1 = pd.DataFrame({"a": [2, 3, 4], "b": [5, 6, 7], "key1": [1, 2, 3], "key2": [5, 2, 3]})
df2 = pd.DataFrame({"c": [1, 2, 9], "d": [5, 8, 9], "key1": [1, 2, 3], "key2": [5, 2, 3]})

print(df1)
print("*************************************")
print(df2)
print("*************************************")
print(pd.merge(df1, df2, how="inner", on="key1"))
print("*************************************")
print(pd.merge(df1, df2, how="inner", on=["key1", "key2"]))
print(pd.merge(df1, df2, how="inner", on="key1"))
print("*************************************")

# Other operations
x = pd.DataFrame({"a": [3, 5, 4, 2, 1], "b": [40, 40, np.nan, 20, 20]})
print(x)
print("*************************************")
print(x.index)
print("*************************************")
print(x.columns)
print("*************************************")
print(x["b"].sum())
print("*************************************")

def inc(x):
    x = x +100
    return x

print(x["b"].apply(inc))

print("*************************************")
print(x.index)

print("*************************************")
print(x.sort_values("a"))
print("*************************************")
print(x["b"].unique())
print("*************************************")
print(x["b"].nunique())
print("*************************************")
print(x["b"].value_counts())
print("*************************************")
print(x.isnull())

 # Loading files


