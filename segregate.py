#2. Take a binary input form user and segregate all 1's to left side and 0's to right side.

#Ex: Input : 1010011 Output : 111100

import numpy as np

lst = np.array(list(input("Enter Binary NO ")))
lst = np.sort(lst)[::-1]
sort_list = "".join(lst)
print(sort_list)