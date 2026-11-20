from database_functions import *
from rental_functions import *

MENU = """Welcome to Minimal Car Company
0. Check Cars left
1. Rent Car(s)
2. Return Car(s)
3. Read T & C
4. Quit
>>> """


def read_terms_conditions():
    """Read terms and conditions in a nicely formatted way."""
    in_file = open("terms.txt", "r", encoding="utf-8")
    line_count = 0
    for line in in_file.readlines():
        line_count += 1
        print(line.strip())
        if line_count % 10 == 0:
            input("Press Enter to continue...")

    in_file.close()


def main():
    """Start of program."""
    availability = read_availability()        # read from file
    choice = input(MENU)  # 1. init

    while choice != "4":  # 2. condition
        # 3. body
        if choice == "0":
            print("0. Check Cars left")
            print(f"There is/are {availability} car(s) left.")
        elif choice == "1":
            print("1. Rent Car")
            availability = rent_car(availability)
        elif choice == "2":
            print("2. Return Car")
            availability = return_car(availability)
        elif choice == "3":
            print("3. Read T & C")
            read_terms_conditions()
        else:
            print("Invalid choice!")

        choice = input(MENU)  # 4. alter choice

    # 5. outside of while loop
    write_availability(availability)       # write back to file
    print("-- File saved --")

main()