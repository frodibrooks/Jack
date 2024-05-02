# import correct packages
import matplotlib.pyplot as plt
import numpy as np


# Pose location
file_path = "/Users/frodibrooks/Desktop/DTU/2.önn/Building_Dependable/log_20240404_121729.277/log_pose.txt"



# Logged values
data = []
time = []
vel_r = []
vel_l = []
robot_vel = []
turn_rate = []
turn_radius = []
x = []
y = []
theta = []
driven_dist = []
turned_angle = []



with open(file_path,"r") as file:
    for line in file:
        words = line.split()

        if len(words) >= 10:
            time.append(float(words[0]))
            vel_l.append(float(words[1]))
            vel_r.append(float(words[2]))
            robot_vel.append(float(words[3]))
            turn_rate.append(float(words[4]))
            turn_radius.append(float(words[5]))
            x.append(float(words[6]))
            y.append(float(words[7]))
            theta.append(float(words[8]))
            driven_dist.append(float(words[9]))
            turned_angle.append(float(words[10]))




def initialize_time(time):
    initial_value = time[0]
    for i in range(len(time)):
        time[i] = time[i] - initial_value
    return time
    
time = initialize_time(time)



x_run2 = x[:(len(x)//10)]
y_run2 = y[:(len(y)//10)]



time_ir = []
sensor1 = []
sensor2 = []
s1_filtered = []
s2_filtered = []


with open("/Users/frodibrooks/Desktop/DTU/2.önn/Building_Dependable/log_20240404_121729.277/log_irdist_sensor.txt","r") as file:
    for line in file:
        words = line.split()
        time_ir.append(float(words[0]))
        sensor1.append(float(words[1]))
        sensor2.append(float(words[2]))
        s1_filtered.append(float(words[3]))
        s2_filtered.append(float(words[4]))
        

time_ir = initialize_time(time_ir)



driven_dist = driven_dist[:(len(driven_dist))//10]
time = time[:(len(time)//10)]
robot_vel = robot_vel[:(len(robot_vel)//10)]


time_ir = time_ir[:(len(time_ir)//10)]
sensor1 = sensor1[:(len(sensor1)//10)]
sensor2 = sensor2[:(len(sensor2)//10)]
s1_filtered = s1_filtered[:(len(s1_filtered)//10)]
s2_filtered = s2_filtered[:(len(s2_filtered)//10)]



time_mixer = []
vel_mixer = []

with open("/Users/frodibrooks/Desktop/DTU/2.önn/Building_Dependable/log_20240404_121729.277/log_mixer_values.txt","r") as file:
    for line in file:
        words = line.split()
        time_mixer.append(float(words[0]))
        vel_mixer.append(float(words[2]))
        

time_mixer = initialize_time(time_mixer)
time_mixer = time_mixer[:(len(time_mixer)//18)]
vel_mixer = vel_mixer[:(len(vel_mixer)//18)]


print(len(time_mixer), len(vel_mixer))


plt.title("Measured robot velocity, set velocity and distance driven over time")
plt.grid()
# plt.plot(time, driven_dist_run2, label='Driven distance')
plt.plot(time, robot_vel, label='Robot Velocity')
plt.plot(time_mixer, vel_mixer, label='Set velocity')
plt.plot(time, driven_dist, label='Driven distance')



# plt.plot(time_ir,sensor2,label = 'IR sensor 2')
# plt.plot(time_ir,sensor1,label = 'IR sensor 1')
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Distance [m]")
plt.show()




# plt.title("X vs Y: Odometry coordinates [m]")
# plt.grid()
# plt.plot(x_run2,y_run2)
# plt.show()

