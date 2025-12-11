def calculate_rectangle_area():
    # Get user input for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate the area
    area = length * width
    
    # Display the result
    print(f"The area of the rectangle is {area}")

# Call the function
calculate_rectangle_area()

def calculate_rectangle_volume():
    # Get user input for length and width and height
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    
    # Calculate the volume
    volume = length * width * height
    
    # Display the result
    print(f"The volume of the rectangle is {volume}")

# Call the function
calculate_rectangle_volume()