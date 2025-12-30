import random
from flask import Flask, render_template
import time
from calculations import *
current_fps = 0.0
total_distance = 0.0 
longest_run = 0.0
lastTime = 0.0 

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data - replace with actual values

    return render_template('index.html',
                         speed=current_fps,
                         distance=total_distance,
                         duration=longest_run)

#if __name__ == '__main__':
#   app.run(debug=True)


def sensorTripped():
    global current_fps 
    global total_distance
    global longest_run
    global lastTime
    currentTime = time.time()   
    if lastTime != 0.0:
        timeDiff = currentTime - lastTime
        if timeDiff > 5: #assume the cat has started a new run if more than 5 seconds have passed
            longest_run = max(longest_run, total_distance)
            total_distance = 0.0
        else:
            current_fps = distance_between_sensors(radius, sensor_count) / timeDiff 
            total_distance += distance_between_sensors(radius, sensor_count)
    lastTime = currentTime
    print(f"Current FPS: {current_fps}, Total Distance: {total_distance}, Longest Run: {longest_run}")





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
