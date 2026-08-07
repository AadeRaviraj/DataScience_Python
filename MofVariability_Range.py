import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 




border = "-" * 90

# read Dataset by csv 

data = pd.read_csv("Dataset\TitanicDataset.csv")

print(data.head)

print(border)

print("---------------  minimum value  ------------------")

min_value = data["Age"].min()
print("Min Value : ",min_value)

print(border)

print('------------------- Maximum Value -------------------')

max_value = data["Age"].max()

print("Max Value : ",max_value)

print(border)

print("-------------------- Range Value -------------------")

range_value = min_value - min_value

print(range_value)
