import pandas as pd
import numpy as np


def DataFrameGenerator():
    col_string = input("Enter the column names, one after the other, separated by space.")
    print(f"You have entered: '{col_string}'")
    col = col_string.split()
    length_of_row = len(col)
    print(f"Number of columns: {length_of_row}")
    number_of_rows = int(input("How many rows do you want? Input an integer."))
    counter = 0
    rows = []
    while counter < number_of_rows:
        print(f"Counter: {counter}")
        raw_input = input(f"Type in the {counter+1}. row. {number_of_rows - counter} Rows remaining. Make sure to only type {length_of_row} numbers, separated by space.")
        row_as_string = raw_input.split()
        row = []
        for number in row_as_string:
            row.append(int(number))
        rows.append(row)
        counter += 1
    data = pd.DataFrame(columns=col, data=np.array(rows))
    return data
