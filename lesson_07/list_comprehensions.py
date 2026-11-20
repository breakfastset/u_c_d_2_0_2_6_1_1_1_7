# list comprehension is a shorthand in writing
# a for loop to collect items into a list
# list_name = [ x for x in items ]

scores = [45, 67, 89, 32, 50, 70]  # out of 100

scores_2 = [x for x in scores]   # copy of scores
print("scores_2:", scores_2)
scores_3 = [x/10 for x in scores]
print("scores_3:", scores_3)

passes = [x for x in scores if x >= 50]
failures = [x for x in scores if x < 50]
print("passes:", passes)
print("failures:", failures)

print()
grades = ['p' if x >= 50 else 'f' for x in scores]
print("grades:", grades)
print("--" * 20)

# write the equivalent using a conventional for-loop
grades_1 = []
for x in scores:
    if x >= 50:
        grades_1.append('p')
    else:
        grades_1.append('f')
print("grades_1:", grades_1)




