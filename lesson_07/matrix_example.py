seatings = [
    ["Jo", "Mia", "Cookie"],     # 0    -4
    ["Low", "Tee", "Leh"],       # 1    -3
    ["Tata", "Mama", "Siti"],    # 2    -2
    ["Cay", "Kim", "Tong"]       # 3    -1
]   #  0      1       2
    #  -3    -2      -1

print("Row #1: ", seatings[1])  # ['Low', 'Tee', 'Leh']
print("seatings[0][0]: ", seatings[0][0])   # Jo
print("seatings[2][1]: ", seatings[2][1])   # Mama
print("seatings[-1][-1]: ", seatings[-1][-1])  # Tong
print("--" * 20)
print("\n\n\n")

for row in range(len(seatings)):
    current_row = seatings[row]
    for column in range(len(current_row)):
        print(f"{current_row[column]:10}", end=" ")
    print()


