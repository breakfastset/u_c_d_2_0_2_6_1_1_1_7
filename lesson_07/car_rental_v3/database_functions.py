CARS_FILE = "cars.txt"

def read_availability():
    """Read availability from file."""
    car_list = []     # list of lists (cars)
    in_file = open(CARS_FILE, "r")
    for line in in_file:
        car_data = line.split(",")
        car_data[-1] = int(car_data[-1])   # convert to int
        car_list.append(car_data)
    in_file.close()
    return car_list      # list of cars


def write_availability(availability):
    """Write updated availability back to file."""
    out_file = open(CARS_FILE, "w")

    out_file.close()