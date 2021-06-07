#4. Write a Python program to test whether each element of a 1-D array is also present in a
#second array.
#Expected Output:
#Array1: [ 0 10 20 40 60]
#Array2: [0, 40]
#Compare each element of array1 and array2
#[ True False False True False]

import numpy as np

Array1 = [ 0, 10, 20, 40, 60]
Array2 = [0, 40,60]
res = np.isin(Array1, Array2)
print(res)