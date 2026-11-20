from database_functions import *

# return a list of lists
# [
#    ['BYD', 'Seal', 'B', 5],
#    ['Hyundai', 'Avante', 'A', 7],
#    ...
# ]
def main():
    """Test database functions."""
    cars = read_availability()
    print(cars)
    # write_availability(cars)

main()