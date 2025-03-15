import random
import os

f = 10000
scale = [10 * f,20 * f,30 * f,40 * f,50 * f]
sort_type = ["bubble_sort","insert_sort","select_sort","merge_sort","quick_sort"]
root_dir = ".\\resource"

def generate_data(path,sc):
    with open(path,"w") as file:
        file.write(str(sc) + "\n")
        for i in range(sc):
            file.write(str(random.randint(0,100000)) + " ")

for i in range(0,len(sort_type)):

    sort_path = root_dir
    if not os.path.exists(sort_path):
            os.mkdir(sort_path)

    for j in range(0,len(scale)):
        sc_dir = str(int(scale[j] / 1000)) + "k"
        sc_path = os.path.join(sort_path,sc_dir)
        if not os.path.exists(sc_path):
            os.mkdir(sc_path)
        for idx in range(1,21):
            datafile_name = str(idx) + ".txt"
            datafile_path = os.path.join(sc_path,datafile_name)
            generate_data(datafile_path,scale[j])
            
                     



