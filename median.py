import numpy as np 
import pandas as pd 



border = "=" * 70


arr = np.array([40, 30, 20 , 10 , 50])
asc_order = np.sort(arr)

print(border)
print("Sorted array (Asc Order): ", asc_order)
print(border)

desc_order = np.sort(arr)[::-1] # output should be 50 , 40 , 30, 20 , 10
print(border)
print("Descending order : ", desc_order )
print(border)

# get median value 

print(border)
print("Calculate median value of odd sequence : ")
print(border)

median_value = np.median(arr)
print("Median Value : ",median_value)
print(border)



