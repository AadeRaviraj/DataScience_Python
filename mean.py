import numpy as np 
import pandas as pd 

arr = np.array([2,4,3,5,6,7,8,2,4,8,9,3,5,6,7,8,8,8])

sum = np.sum(arr)
print(sum)

length_arr = len(arr)
print(length_arr)

mean_average = sum / length_arr

print("Average of all values :", mean_average)


sorted_Data = np.sort(arr)
print(sorted_Data)