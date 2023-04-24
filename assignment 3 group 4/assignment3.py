print("Welcome to Shiny Paint Company for indoor painting!")

coverage_per_gallon = 350
cost_per_gallon = 42
labour_cost_per_squarefeet = 0.5

# Function to calculate the area of a wall,window and door
def wall_area(length, height):
    return length * height
def windows_area(length, height):
    return length * height
def doors_area(length, height):
    return length * height

# Function to calculate the surface area to be painted for a wall in a room
def paint_area(wall_area, windows_area, doors_area):
    return wall_area - sum(windows_area) - sum(doors_area)

# Function to calculate the gallons of paint required for a room
def paint_gallons(paint_area):
    return paint_area / coverage_per_gallon

# Function to calculate the cost of painting a room
def room_cost(paint_gallons):
    return (paint_gallons * cost_per_gallon) + (paint_gallons * labour_cost_per_squarefeet)

# Initialize variables for the total surface area, gallons of paint required, and cost of painting the house
total_surface_area = 0
total_paint_gallons = 0
total_cost = 0

# Ask the user for the number of rooms in the house
num_rooms = int(input("How many rooms do you want to paint?: "))
print("Thank you!")

# Loop over each room and collect information
for i in range(num_rooms):
    print(f"Room: {i+1}")
    # room_type = input("Is this room square, rectangular, or custom? ")
    print(("Please select the shape of the room:\n 1 - Rectangular\n 2 - Square\n 3 - Custom (more or less than 4 walls, all square or rectangles)"))
    shape = int(input())
    
    if shape =="square":
        length = float(input("What is the length of the wall in feet? "))
        height = float(input("What is the height of the wall in feet? "))
        wall_area = length * height
        paint_area = paint_area(wall_area, [], [])
        gallons = paint_gallons(paint_area)
        cost = room_cost(gallons)
        print(f" for Room: {i+1}, the area to be painted: {wall_area} sq.ft and will require {gallons:.2f} to paint. This will cost the customer ${cost:.2f}")
        
        total_surface_area += wall_area
        total_paint_gallons += gallons
        total_cost += cost
   
    elif shape =="rectangular":
        length = float(input("What is the length of the room in feet? "))
        width = float(input("What is the width of the room in feet? "))
        height = float(input("What is the height of the room in feet? "))
        wall_area = 2 * ((length * height) + (width * height))
        gallons = paint_gallons(paint_area)
        cost = room_cost(gallons)
        print(f" for Room: {i+1}, the area to be painted: {wall_area} sq.ft and will require {gallons:.2f} to paint. This will cost the customer ${cost:.2f}")
    else:
        length = float(input("What is the length of the room in feet? "))
        width = float(input("What is the width of the room in feet? "))
        height = float(input("What is the height of the room in feet? "))
        wall_area = 2 * ((length * height) + (width * height))
        gallons = paint_gallons(paint_area)
        cost = room_cost(gallons)
        print(f" for Room: {i+1}, the area to be painted: {wall_area} sq.ft and will require {gallons:.2f} to paint. This will cost the customer ${cost:.2f}")
        
        num_windows = int(input("how many windows are in the room"))
        for j in range(num_windows):
            window_width = float(input(f"What is the width of window {j+1} in feet? "))
            window_height = float(input(f"What is the height of window {j+1} in feet? "))
            window_area = window_width * window_height
            windows_area.append(window_area)
        doors = []
        
        num_doors = int(input("How many doors are in the room? "))
        for j in range(num_doors):
            door_width = float(input(f"What is the width of door {j+1} in feet? "))
            door_height = float(input(f"What is the height of door {j+1} in feet? "))
            door_area = door_width * door_height
            doors.append(door_area)
        paint_area = paint_area(wall_area, windows_area, doors_area)
        gallons = paint_gallons(paint_area)
        cost = room_cost(gallons)
        
        print(f" for Room: {i+1}, the area to be painted: {wall_area} sq.ft and will require {gallons:.2f} to paint. This will cost the customer ${cost:.2f}")

