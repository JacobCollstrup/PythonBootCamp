# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import numpy as np
import pandas as pd
import plotly as pl
import cufflinks as cf
import plotly.offline as po

po.init_notebook_mode(connected=True)

cf.go_online()

df1 = pd.DataFrame(np.random.rand(100,5), columns=["a", "b", "c", "d", "e"])
df2 = pd.DataFrame({"x":["a", "b", "c", "d", "e"], "y":[1, 2, 3, 4, 5], "z": [6, 7, 8, 4, 3]})
df1.iplot(kind="scatter")
