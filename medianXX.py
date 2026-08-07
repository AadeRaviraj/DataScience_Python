import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 




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
# print("Average using in-build method : ",data["Age"].mean()) 
# using numpy 
mn = np.mean(data["Age"])
print("Average using numpy ", mn )
print(line)

print("----------------------------- data showing bu using seaborn --------------------- ")
sns.histplot(x="Age", data=data, bins=[i for i in range(0, 81, 10)])
plt.plot([mn for i in range(0 , 700)], [i for i in range(0 , 700)], c = "red")
plt.show()
