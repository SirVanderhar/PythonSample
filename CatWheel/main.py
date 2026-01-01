import random
import time
from datetime import datetime
from calculations import *
from os import path 

basepath = path.dirname(__file__)

current_fps = 0.0
total_distance = 0.0 
longest_run = 0.0
lastTime = 0.0 
radius = 3.5 #radius of the wheel in feet
sensor_count = 2 #number of sensors on the wheel



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
        if timeDiff > 5: 
            #assume the cat has started a new run if more than 5 seconds have passed
            #call function to save the last run data into a text file for later analysis
            saveData(lastTime)
            #saveHTML(lastTime)
            longest_run = max(longest_run, total_distance)
            total_distance = 0.0
            startOfNewRun = currentTime
        else:
            current_fps = distance_between_sensors(radius, sensor_count) / timeDiff 
            total_distance += distance_between_sensors(radius, sensor_count)
            saveHTML(currentTime)
    lastTime = currentTime
    print(f"Current FPS: {current_fps}, Total Distance: {total_distance}, Longest Run: {longest_run}")

#function to save data to a text file
#timestamp the file with the current date and time
#append the last run distance to the file
def saveData(savetime: float):
    timestamp = datetime.fromtimestamp(savetime).strftime('%Y%m%d_%H%M%S')
    #timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filepath = path.abspath(basepath + f"/logs/catwheel_data_{timestamp}.txt")
    with open(filepath, "a") as f:
        f.write(f"Last Run total distance:{total_distance: .2f}\n")

def saveHTML(savetime: float):
    #function to save data to an HTML file for web display
    with open("catwheel_data.html", "w") as f:
        f.write("<html><body>\n")
        f.write(f"<h1>Data as of {datetime.fromtimestamp(savetime).strftime('%Y-%m-%d %H:%M:%S')}</h1>\n")
        f.write(f"<h1>Current FPS: {current_fps: .1f}</h1>\n")
        f.write(f"<h1>Total Distance: {total_distance: .1f} in feet</h1>\n")
        f.write(f"<h1>Longest Run: {longest_run: .1f} in feet</h1>\n")
        f.write("</body></html>\n")




#simulate sensor triggers for testing
#hardware will call sensorTripped() when a sensor is triggered with reed switches attached to the wheel and gpio pins on raspberry pi

if __name__ == "__main__":
    #print("Simulating sensor triggers...")
    #print("Press Ctrl+C to stop.")
    #print("Wheel radius:", radius, "feet. Number of sensors:", sensor_count, "Distance between sensors:", distance_between_sensors(radius, sensor_count), "feet.","/n")
    for _ in range(random.randint(10, 40)):
        sensorTripped()
        time.sleep(random.uniform(0.1, .5))
    time.sleep(6)  # simulate a pause longer than 5 seconds
    for _ in range(random.randint(10, 40)):
        sensorTripped()
        time.sleep(random.uniform(0.1, .5))
    time.sleep(6)
    for _ in range(random.randint(10, 40)):
        sensorTripped()
        time.sleep(random.uniform(0.1, .5))
