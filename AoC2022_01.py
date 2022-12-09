import numpy as np

with open("data.txt", "r") as file:
    data = file.read()
    
elves = np.array(data.split('\n\n'))

#part 1
max_cal = 0
max_cal_2 = np.array([0,0,0])

for elf in elves:
    calories = np.array([int(x) for x in elf.split('\n')]).sum()
    if calories > max_cal:
        max_cal = calories
    if calories > max_cal_2[0]:
        max_cal_2 = np.append(max_cal_2[1:],calories)
        max_cal_2.sort()
    
print(max_cal)
print(max_cal_2.sum())