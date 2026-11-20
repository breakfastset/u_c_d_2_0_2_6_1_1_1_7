def rent_car(availability):
    """Rent car if available and update availability."""
    num_cars = int(input("Enter number of cars: "))
    if 0 < num_cars <= availability:
        availability -= num_cars
        print(f"Your {num_cars} car(s) is/are available at checkout.")
    else:
        print(f"Sorry, we do not have {num_cars} cars available at the moment.")
    return availability

def return_car(availability):
    """Return car and update availability."""
    num_cars = int(input("Enter number of cars: "))
    if num_cars > 0:
        availability += num_cars
        print("Thank you for returning our cars in one piece.")
    else:
        print("Invalid number of cars. (must be > 0)")
    return availability
