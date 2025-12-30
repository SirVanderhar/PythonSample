import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#get current data from file
file = open("/home/pi/current_count","r")
feet_traveled = float(file.readline())
high_mph = float(file.readline())
max_mph_time = file.readline()

prev_time = 0
mark_time = 0
prev_feet_traveled = 0
mph = 0

def increase_count(channel):
    global prev_time
    global feet_traveled
    global prev_feet_traveled
    global high_mph
    global max_mph_time
    global mph

    feet_traveled += 2.095
    mark_time = time.time()
    elapsed_time = mark_time - prev_time
    prev_time = mark_time
    fps = (feet_traveled - prev_feet_traveled) / elapsed_time
    prev_feet_traveled = feet_traveled
    mph = fps / 0.6818182

    if mph > high_mph:
        high_mph = mph
        max_mph_time = time.asctime(time.localtime(time.time()))

    print('Feet per second  = ' + str(fps))
    print('MPH = ' + str(mph))
    print('Highest MPH ' + str(high_mph))

    # write mph log
    with open('/home/pi/mph_log', 'a+') as writer:
       localtime = time.asctime(time.localtime(time.time()))
       mph_log = localtime + ' MPH {0} fps {1}'.format(mph,fps) + '\n'
       writer.write(mph_log)

GPIO.add_event_detect(6, GPIO.RISING, callback=increase_count, bouncetime=300)

while True:
    miles_traveled = float(feet_traveled)/5280
    print("Distance traveled is {0:,.1f} feet or {1:.3f} miles".format(feet_traveled,miles_traveled))
    sleep(10)
    distance = "<h1>Distance traveled is {0:,.1f} feet or {1:.3f} miles".format(feet_traveled,miles_traveled)
    max_mph = '<h1>Peak MPH was {0:.2f} at '.format(high_mph) + str(max_mph_time)
    current_mph = '<h1>Last speed measured was {0:.2f}mph'.format(mph) 

    # write web page
    with open('/var/www/html/index.html', 'w') as writer:
       writer.write('<html><body>' + distance)
       writer.write('</h1>')
       writer.write(current_mph)
       writer.write('</h1>')
       writer.write(max_mph + '</body></html>')

    # write current count to disk
    with open('/home/pi/current_count', 'w') as writer:
       writer.write(str(feet_traveled) + '\n')
       writer.write(str(high_mph) + '\n')
       writer.write(max_mph_time)

    # write to log file
    with open('/home/pi/log_file', 'a+') as writer:
       localtime = time.asctime(time.localtime(time.time()))
       distance = localtime + ' Distance traveled is {0:,.1f} feet or {1:.3f} miles'.format(feet_traveled,miles_traveled) + '\n'
       writer.write(distance)