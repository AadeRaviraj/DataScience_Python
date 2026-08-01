import numpy as np 
import pandas as pd 



line = " - " * 40

# read Dataset by csv 

data = pd.read_csv("Dataset\TitanicDataset.csv")

print(data.head)

# show all age name data 

print(line)
print("-----------------------------  Show all age column data -------------------------")
print(data["Age"])
print(line)

print(line)

print("--------------------------- Average of age column -------------------------------")
print("Average using in-build method : ",data["Age"].mean()) 
# using numpy 
print("Average using numpy ", np.mean(data["Age"]))
print(line)
