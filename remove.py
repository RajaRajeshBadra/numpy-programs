# 3. Write a Python program to remove the nth index character from a nonempty string.

import numpy as np

print("Enter a string: ")
str = np.array(list(input()))
print("Enter index to be removed: ")
index = int(input())
if (index >= len(str)):
  print("Out of range!!")
else:
  str = np.delete(str,index)
  res = "".join(str)
  print(res)