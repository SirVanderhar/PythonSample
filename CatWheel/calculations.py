
#radius of the wheel in feet 
radius = 1.3
#number of sensors on the wheel
sensor_count = 6


# calculate the distance between sensors on a circular path 
def distance_between_sensors(radius, sensor_count):
    import math
    angle = math.pi / sensor_count
    distance = 2 * radius * math.sin(angle)
    return distance 


