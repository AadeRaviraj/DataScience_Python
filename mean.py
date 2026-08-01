import numpy as np 
import pandas as pd 

# create an array 
arr = np.array([2,4,3,5,6,7,8,2,4,8,9,3,5,6,7,8,8,8])

# sum of all array 
sum = np.sum(arr)
print("Sum of all array : ",sum)


# calculate length of array 
length_arr = len(arr)
print("Length of array : ",length_arr)

# calculate mean by manually 
mean_average = sum / length_arr
print("Manually calculate mean :", mean_average)



# Using in-build method calculate mean 

mean_cal = np.mean(arr)
print("Calculate mean using in-build method : ", mean_cal)

# sort data 
sorted_Data = np.sort(arr)
print("Sorted Array ",sorted_Data)


