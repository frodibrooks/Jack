
import matplotlib.pyplot as plt
import numpy as np


file_path = "/Users/frodibrooks/Desktop/DTU/2.önn/Building_Dependable/log_20240404_121729.277/log_gyro_values.txt"

time = []
x = []
y = []
z = []

with open(file_path,"r") as file:
    for line in file:
        words = line.split()
        time.append(float(words[0]))
        x.append(float(words[1]))
        y.append(float(words[2]))
        z.append(float(words[3]))
        




def initialize_time(time):
    initial_value = time[0]
    for i in range(len(time)):
        time[i] = time[i] - initial_value
    return time

time = initialize_time(time)

time = time[:(len(time)//10)]
x = x[:(len(x)//10)]
y = y[:(len(y)//10)]
z = z[:(len(z)//10)]


plt.plot(time,x ,label='gyro x')
plt.plot(time,y ,label='gyro y')
plt.plot(time,z ,label='gyro z')
plt.legend()
plt.xlabel("time [s]")
plt.ylabel("Degrees/s")
plt.show()