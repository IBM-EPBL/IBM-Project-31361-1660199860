# -*- coding: utf-8 -*-
"""PNT2022TMID23204.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dxgtpjK7r4T9I2e6PgbL5BoMnkCIJ5CV
"""

s = "Hi there Sam"

"""2. Use .format() to print the following string.
Output should be: The diameter of Earth is 12742 kilometers.
"""

print(s.split())

planet = "Earth"
diameter = 12742

print("The diameter of Earth is {diameter} kilometers.")

"""3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

import numpy as np

zeros=np.zeros(10)
fives=np.full(10,5)
print(zeros,fives)

""". Create an array of all the even integers from 20 to 35"""

arr=[i for i in range(20,35+1) if i%2==0]
arr

"""6. Create a 3x3 matrix with values ranging from 0 to 8"""

array=np.arange(0,9).reshape((3,3))
array

"""7. Concatenate a and b
a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c=np.concatenate((a,b))

"""Pandas
8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd
d={'name':['raj','jhon','joe'],'age':[21,26,28]}
df=pd.DataFrame.from_dict(d)
df

"""9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

date=pd.date_range("01-01-2023","10-02-2023",freq="D")

"""10. Create 2D list to DataFrame
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df=pd.DataFrame(lists,columns=["C1","C2","C3"])
df