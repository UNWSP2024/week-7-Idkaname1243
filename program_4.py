# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
import math
def calculate_distance(point1, point2):
    try:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return distance
    except Exception as e:
        print(f"Error: {e}")
        return None
def main():
    try:
        x1 = float(input("Enter x-coordinate of the first point: "))
        y1 = float(input("Enter y-coordinate of the first point: "))
        z1 = float(input("Enter z-coordinate of the first point: "))
        point1 = (x1, y1, z1)
        x2 = float(input("Enter x-coordinate of the second point: "))
        y2 = float(input("Enter y-coordinate of the second point: "))
        z2 = float(input("Enter z-coordinate of the second point: "))
        point2 = (x2, y2, z2)
        distance = calculate_distance(point1, point2)
        if distance is not None:
            print(f"The distance between the points {point1} and {point2} is: {distance}")
    except ValueError:
        print("Invalid input. Please enter valid numeric coordinates.")
if __name__ == "__main__":
    main()
