import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 




border = " - " * 40

# read Dataset by csv 

data = pd.read_csv("Dataset\TitanicDataset.csv")

print(data.head)

print(border)

print("---------------  minimum value  ------------------")

print(border)

print('------------------- Maximum Value -------------------')

print(border)
