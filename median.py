import numpy as np 
import pandas as pd 



border = " - " * 40


arr = np.array([40, 30, 20 , 10 , 50])
asc_order = np.sort(arr)

print(border)
print("Sorted array : ", asc_order)
print(border)

desc_order = np.sort(arr)[::-1]
print(border)
print("Descending order : ", desc_order )
print(border)


# get median value 



