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

# median_value = np.median(arr)  # using in-build method 
# print("Median Value : ",median_value)
# print(border)
# print(border)
length  = len(arr)

median = asc_order[length // 2]   # calculate odd series median value 
print(median)
print(border)

print(border)
print("----------------------------- Calculate Even Series median value -------------------")

arr2 = np.array([40, 30, 20 , 10 , 50,60])
sorted_arr = np.sort(arr2)

print(border)
print("Even Series Sorted values : ", sorted_arr)
print(border)



print() 
print("Calculate even series median ")

even_series =  (sorted_arr[len(sorted_arr) // 2 -1 ] + sorted_arr[len(sorted_arr) // 2]) / 2

print("Even Series median value : ", even_series)

print(border)
