# import correct packages
import matplotlib.pyplot as plt
import numpy as np


# Pose location
file_path = "/Users/frodibrooks/Desktop/DTU/2.önn/Building_Dependable/log_20240404_121729.277/log_pose_abs_values.txt"



# Logged values
data = []
time = []
x = []
y = []
theta = []
driven_dist = []
turned_angle = []



with open(file_path,"r") as file:
    for line in file:
        words = line.split()
        time.append(float(words[0]))
        x.append(float(words[1]))
        y.append(float(words[2]))
        theta.append(float(words[3]))
        driven_dist.append(float(words[4]))
        turned_angle.append(float(words[5]))







def initialize_time(time):
    initial_value = time[0]
    for i in range(len(time)):
        time[i] = time[i] - initial_value
    return time
    
time = initialize_time(time)

x = x[:(len(x)//10)]
y = y[:(len(y)//10)]





filename1 = "/Users/frodibrooks/Desktop/DTU/2.önn/Building_Dependable/log_20240404_121100.247/log_pose_abs_values.txt"

x_run1 = []
y_run1 = []

with open(file_path,"r") as file:
    for line in file:
        words = line.split()
        x_run1.append(float(words[1]))
        y_run1.append(float(words[2]))


x_run1 = x_run1[:(len(x_run1)//10)]
y_run1 = y_run1[:(len(y_run1)//10)]


plt.title("x and y coordinates")
plt.grid()
plt.plot(x,y,label = "run2")
# plt.plot(x_run1,y_run1,"--", label = "run1")
plt.legend()
plt.show()