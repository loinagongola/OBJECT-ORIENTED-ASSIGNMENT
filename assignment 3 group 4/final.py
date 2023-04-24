def welcome_message():
    print("Welcome to Shiny Paint Company for indoor painting!")


def get_num_rooms():
    num_rooms = int(input("How many Rooms do you want to paint:\n"))
    print("Thank you!")
    return num_rooms


def computeRoomArea(room_num):
    print("Room:", room_num)
    print("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)")
    shape = int(input())
    if shape == 1:
        area = computeRectangleWallsArea()
    elif shape == 2:
        area = computeSquareWallsArea()
    elif shape == 3:
        area = computeCustomWallsArea()
    else:
        print("Invalid input!")
        return 0  # return a default value if input is invalid

    window_door_area = computeWindowsDoorsArea()
    area -= window_door_area

    gallons = computeGallons(area)
    cost = computePaintPrice(area)

    print("For Room:", room_num, ", the area to be painted is", "{:.2f}".format(area), "square ft and will require", "{:.2f}".format(
        gallons), "gallons to paint. This will cost the customer $", "{:.2f}".format(cost))

    return area  # return the computed area value


def computeRectangleWallsArea():
    length = float(input("Enter the length of the room in feet:\n"))
    width = float(input("Enter the width of the room in feet:\n"))
    height = float(input("Enter the height of the room in feet:\n"))

    area = 2 * ((length * height) + (width * height))
    return area


def calculateRectangleArea(length, width):
    return length * width


def computeSquareWallsArea():
    side_length = float(input("Enter the length of one side of the room:\n"))
    area = 4 * calculateRectangleArea(side_length, side_length)
    return area


def computeWindowsDoorsArea():
    num_windows = int(input("How many windows/doors does the room contain?\n"))
    area = 0
    for i in range(num_windows):
        print("Enter window", i+1, "dimensions:")
        length = float(input("Length in feet: "))
        width = float(input("Width in feet: "))
        area += calculateRectangleArea(length, width)
    return area


def computeCustomWallsArea():
    num_walls = int(input("How many walls are there in the room\n"))
    area = 0
    for i in range(num_walls):
        print("Enter dimensions for wall", i+1)
        height = float(input("Height in feet: "))
        length = float(input("Length in feet: "))
        area += calculateRectangleArea(length, height)
    return area


def computeGallons(area):
    return (area/350)


def computePaintPrice(area):
    gallons = computeGallons(area)
    return gallons * 42


# Main program
welcome_message()
num_rooms = get_num_rooms()
total_area = 0
total_gallons = 0
total_cost = 0

for i in range(num_rooms):
    room_area = computeRoomArea(i+1)
    total_area += room_area 
    total_gallons += computeGallons(room_area)
    total_cost += computePaintPrice(room_area)

print("Total area to be painted is", "{:.2f}".format(total_area), "square ft and will require", "{:.2f}".format(
    total_gallons), "gallons of paint. This will cost the customer $", "{:.2f}".format(total_cost))
