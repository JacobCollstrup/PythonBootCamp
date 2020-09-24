import pandas as pd
import numpy as np
from DataFrameGenerator import DataFrameGenerator
"""
string = "This is some words"

list_of_words = string.split()

# for word in list_of_words:
#     print(word)


column_names = ["Col1", "Col2", "Col3", "Col4", "Col5"]

row1 = np.random.randint(low=0,high=10, size=5)
row2 = np.random.randint(low=0,high=10, size=5)
row3 = np.random.randint(low=0,high=10, size=5)
row4 = np.random.randint(low=0,high=10, size=5)
row5 = np.random.randint(low=0,high=10, size=5)

matrix = []
for i in range(3):
    matrix.append(list(np.random.randint(low=0,high=10, size=5)))

for row in matrix:
    print(row)

np_matrix = np.array(matrix)
print(np_matrix)
print(type(np_matrix))
print(f"Number of rows in matrix: {len(matrix)}")
index = list(range(len(matrix)))
print(index)

df_matrix = pd.DataFrame(columns=column_names, data=np.array(matrix))

print(matrix)
print(df_matrix.head())


df = pd.DataFrame(columns=column_names, data=[row1, row2, row3, row4, row5])

# print(df.head())

numbers_as_strings = "5 6 8 4 9"

list_of_numbers_as_strings = numbers_as_strings.split()
#print(list_of_numbers_as_strings)
numbers = []
for number in list_of_numbers_as_strings:
    #print(number)
    numbers.append(int(number))


#print(numbers)
"""
data = DataFrameGenerator()
print(data.head())