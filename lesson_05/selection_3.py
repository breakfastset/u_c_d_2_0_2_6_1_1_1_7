# 3. if - elif - elif .... else (optional)
# multiple conditions (mutually exclusive)
# A if > 80, B if > 70, C if > 60, D > 50 otherwise F

score = float(input("Enter your score: "))
if 80 <= score <= 100:
    print("Excellent job! Grade A")
elif 70 <= score < 80:
    print("Good job! Grade B")
elif 60 <= score < 70:
    print("Great attempt! Grade C")
elif 50 <= score < 60:
    print("Pass! Try harder! Grade D")
elif 0 <= score < 50:
    print("Fail! Please attempt harder next time! Grade F")
else:
    print("Invalid score! Score must be between 0 to 100")

print("See you again!")