import random
import time
from datetime import datetime
from calculations import *
current_fps = 0.0
total_distance = 0.0 
longest_run = 0.0
lastTime = 0.0 

#function to be called when a sensor is tripped
#updates current fps, total distance, and longest run
def sensorTripped():
    #call global variables to interact with them outside of the function
    global current_fps 
    global total_distance
    global longest_run
    global lastTime
    currentTime = time.time()   
    if lastTime != 0.0:
        timeDiff = currentTime - lastTime
        if timeDiff > 5: #assume the cat has started a new run if more than 5 seconds have passed
            #call function to save the last run data into a text file for later analysis
            saveData(lastTime)
            longest_run = max(longest_run, total_distance)
            total_distance = 0.0
        else:
            current_fps = distance_between_sensors(radius, sensor_count) / timeDiff 
            total_distance += distance_between_sensors(radius, sensor_count)
    lastTime = currentTime
    print(f"Current FPS: {current_fps}, Total Distance: {total_distance}, Longest Run: {longest_run}")

#function to save data to a text file
#timestamp the file with the current date and time
#append the last run distance to the file
def saveData(savetime: float):
    timestamp = datetime.fromtimestamp(savetime).strftime('%Y%m%d_%H%M%S')
    #timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    with open(f"catwheel_data_{timestamp}.txt", "a") as f:
        f.write(f"Last Run total distance:{total_distance}\n")

def saveHTML()



#simulate sensor triggers for testing
#hardware will call sensorTripped() when a sensor is triggered with reed switches attached to the wheel and gpio pins on raspberry pi

if __name__ == "__main__":
    for _ in range(10):
        sensorTripped()
        time.sleep(random.uniform(0.5, 2.0))
    time.sleep(6)  # simulate a pause longer than 5 seconds
    for _ in range(10):
        sensorTripped()
        time.sleep(random.uniform(0.5, 2.0))
