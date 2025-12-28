def calculate_rectangle_area():
    # Get user input for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate the area
    area = length * width
    
    # Display the result
    print(f"The area of the rectangle is {area}")
def calculate_volume_sphere():
    # Get user input for radius
    radius = float(input("Enter the radius of the sphere: "))
    
    # Calculate the volume
    volume = (4/3) * 3.14159 * (radius ** 3)
    
    # Display the result
    print(f"The volume of the sphere is {volume}") 


def choose_shape():
    print("Choose a shape to calculate:")
    print("1. Rectangle Area")
    print("2. Sphere Volume")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        calculate_rectangle_area()
    elif choice == '2':
        calculate_volume_sphere()
    else:
        print("Invalid choice. Please select 1 or 2.")

def calculate_rectangle_volume():
    # Get user input for length and width and height
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    
    # Calculate the volume
    volume = length * width * height
    
    # Display the result
    print(f"The volume of the rectangle is {volume}")