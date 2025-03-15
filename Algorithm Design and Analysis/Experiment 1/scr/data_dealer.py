import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

in_root = ".\\data"
name = os.listdir(in_root)
scale = os.listdir(in_root + "\\bubble_sort")
data = {}
for f in name:
    mean = []
    for sc in scale:
        inpath = os.path.join(in_root,f,sc,"data.txt")
        df = pd.read_table(inpath,sep=" ",header=None)
        df = df.dropna(axis=1,how="all")
        np_arr = df.to_numpy()
        mean.append(np_arr.mean())
    data[f] = np.array(mean).reshape(-1,1)
    
int_scale = np.array([1000000,2000000,3000000,4000000,5000000])
color = ["red","green","blue","purple","black"]
idx = 0
plt.figure(figsize=(10,6))

for key,value in data.items():
    # print(key)
    # print(value)
    
    plt.semilogy(int_scale,value,label=key,color=color[idx])
    idx += 1
    
plt.xlabel("scale")
plt.ylabel("time\ms")
plt.legend()

plt.savefig(".\\result\\result.png")
plt.show()
        