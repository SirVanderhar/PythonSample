# calculate the distance between sensors on a circular path 
def distance_between_sensors(radius, sensor_count):
    import math
    angle = math.pi / sensor_count
    distance = 2 * radius * math.sin(angle)
    return distance 


def feet_to_meters(feet):
    return feet * 0.3048

def feet_to_miles(feet):
    return feet / 5280.0    

def feet_per_second_to_miles_per_hour(fps):
    return fps * 0.68181818

def meters_to_feet(meters):
    return meters / 0.3048  