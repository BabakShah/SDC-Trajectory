from helpers import process_data
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
    return 

def get_x_y(data_list):
    return

def show_x_y(data_list):
    return