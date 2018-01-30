from helpers import process_data
import numpy as np
from math import cos, sin
from matplotlib import pyplot as plt

# %matplotlib inline

data_list = process_data("trajectory_example.pickle")

for entry in data_list:
    print(entry)

def get_speeds(data_list):
    displacement_previous = 0.0
    time_previous = 0.0
    
    speeds = [0.0]
    for i in range(1, len(data_list)):
        displacement = data_list[i][1]
        time = data_list[i][0]
        delta_displacement = displacement - displacement_previous
        delta_time = time - time_previous
        speed = delta_displacement / delta_time
        speeds.append(speed)
        
        displacement_previous = displacement
        time_previous = time
    return speeds

def get_headings(data_list):
    theta_previous = 0.0
    time_previous = 0.0
    thetas = [0.0]
    
    for i in range(1, len(data_list)):
        yaw_rate = data_list[i][2]
        time = data_list[i][0]
        delta_time = time - time_previous
        delta_theta = delta_time * yaw_rate
        theta = theta_previous + delta_theta
        thetas.append(theta)
        
        time_previous = time
        theta_previous = theta
    return thetas

def get_x_y(data_list):
    speeds = get_speeds(data_list)
    thetas = get_headings(data_list)
    x = 0.0
    y = 0.0
    last_time = 0.0
    XY = [(x, y)]    
    for i in range(1,len(data_list)):
        speed = speeds[i]
        theta = thetas[i]
        entry = data_list[i]
        ts, disp, yaw, acc = entry
        dt = ts - last_time
        D  = speed * dt
        dx = D * cos(theta)
        dy = D * sin(theta)
        x += dx
        y += dy
        XY.append((x,y))
        last_time = ts
    return XY

def show_x_y(data_list, increment=1):
    XY = get_x_y(data_list)
    headings = get_headings(data_list)
    X  = [d[0] for d in XY]
    Y  = [d[1] for d in XY]
    h_x = np.cos(headings)
    h_y = np.sin(headings)
    Q = plt.quiver(X[::increment],
                   Y[::increment],
                   h_x[::increment],
                   h_y[::increment],
                   units='x',
                   pivot='tip')
    qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$1 \frac{m}{s}',
                       labelpos='E', coordinates='figure')
    plt.show()

show_x_y(data_list)