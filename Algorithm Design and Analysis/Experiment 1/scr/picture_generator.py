import matplotlib.pyplot as plt
import numpy as np
import os

def fun(path):
    with open(path,"r") as file:
        lines = file.readlines()
        cleaned_lines = [line.strip() for line in lines if line.strip()]
    res = np.loadtxt(cleaned_lines,delimiter=" ",dtype=np.float32)
    return res

root_dir = ".\\data"
data_dir = os.listdir("data")
color = ["red","blue","green","yellow","black"]
X = [1000000,2000000,3000000,4000000,5000000]

cnt = 0
for file_name in data_dir:
    path = os.path.join(root_dir,file_name)
    res = fun(path)
    name = file_name.replace(".txt","")
    print(name)
    plt.plot(X,res,label=name,color=color[cnt],marker="o",linewidth=2,alpha=0.8)
    cnt += 1

plt.legend(loc="best",fontsize=12)
plt.xlabel("Scale",fontsize=14)
plt.ylabel("Time",fontsize=14)

plt.semilogy()

result_path = ".\\result\\result.png"
plt.savefig(result_path,dpi=300)

plt.show()
