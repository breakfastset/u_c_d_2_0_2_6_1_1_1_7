MENU = """Welcome to Minimal Car Company
1. Rent Car
2. Return Car
3. Read T & C
4. Quit
>>> """

CARS_FILE = "cars.txt"

def read_availability():
    """Read availability from file."""
    in_file = open(CARS_FILE, "r")
    line = in_file.readline()    # read the first from file
    availability = int(line)     # convert to integer
    in_file.close()
    return availability          # return number of cars left


def write_availability(availability):
    """Write updated availability back to file."""
    out_file = open(CARS_FILE, "w")
    line = f"{availability}\n"
    out_file.write(line)
    out_file.close()

# Ctrl-/ for mass commenting
# Tab for mass indentation
# Shift Tab for reverse tab
def rent_car(availability):
    """Rent car if available and update availability."""
    if availability > 0:
        availability -= 1
        print("Your car is available at checkout.")
    else:
        print("Sorry, no cars available at the moment.")
    return availability


def return_car(availability):
    """Return car and update availability."""
    availability += 1
    print("Thank you for returning our car in one piece.")
    return availability


def main():
    """Start of program."""
    availability = read_availability()        # read from file
    print(f"There are {availability} cars")   # DEBUG remove later
    choice = input(MENU)
    if choice == "1":
        print("1. Rent Car")
        availability = rent_car(availability)
    elif choice == "2":
        print("2. Return Car")
        availability = return_car(availability)
    elif choice == "3":
        print("3. Read T & C")
        print("... to be updated")
    elif choice == "4":
        print("4. Quit")
        print("Bye bye!")
    else:
        print("Invalid choice!")

    write_availability(availability)                   # write back to file
    print("-- File saved --")

main()