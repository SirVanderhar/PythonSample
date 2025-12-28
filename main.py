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
