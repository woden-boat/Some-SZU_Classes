import random

f = 10000
list = [10 * f,20 * f,30 * f,40 * f,50 * f]
for cnt in range(0,len(list)):
    n = list[cnt]
    data_array = [random.randint(1,100000) for i in range(n)]
    with open("./resource/test_data_" + str(100 * (cnt + 1)) + "k.txt","w") as file:
        file.write(str(n) + '\n')
        for i in data_array:
            file.write(str(i) + ' ')

