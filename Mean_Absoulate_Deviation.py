

border = "-" * 90


data = [10, 20, 30]

print(border)
# Number of values
n = len(data)

print("----------------- Length or list ---------------------")
print("Length of list : ", n)
print(border)

# Total of list
total = sum(data)

print("------------------------- Total of all list -------------------------")
print("Sum of all list : ", total)

print(border)
# mean calculate 

meanValue = total / n

print("----------------------- Mean of all list value -------------------------")
print("Mean Value : ", meanValue)
print(border)

#  Absolute deviations
d1 = abs(data[0] - meanValue)
d2 = abs(data[1] - meanValue)
d3 = abs(data[2] - meanValue)

print("--------------------- Absolute deviation ----------------------------")
print(f'{data[0]} - {meanValue} = {d1}')
print(f'{data[1]} - {meanValue} = {d2}')
print(f'{data[2]} - {meanValue} = {d3}')

print(border)


