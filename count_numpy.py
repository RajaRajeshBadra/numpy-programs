#Using numpy, WAP that takes an input from the user in the form of a list and calculate the
#frequency of occurrence of each character/integer in that list
import numpy as np

lst = []
  
# number of elemetns as input
n = int(input("Enter number of elements : "))
print("nput  elements(integer)")
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele)

(unique, counts) = np.unique(lst, return_counts=True)
frequencies = np.asarray((unique, counts)).T

print(frequencies)