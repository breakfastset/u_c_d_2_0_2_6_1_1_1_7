# reverse
# sort
# sum
# while x in y: y.remove(x) => inefficient

numbers_1 = [5, 6, 1, 3, 4, 9]
numbers_1.reverse()
print(numbers_1)

numbers_1.sort()    # sort in ascending order
print(numbers_1)
numbers_1.sort(reverse=True)   # sort in descending order
print(numbers_1)

total = sum(numbers_1)
print(total)
average = total/len(numbers_1)  # total / 6
print(average)
print("--" * 20)

fruits = ["durian", "mango", "lychee", "durian", "coconut", "durian"]
target = "durian"
while target in fruits:
    fruits.remove(target)
print(fruits)

fruits = ["durian", "mango", "lychee", "durian", "coconut", "durian"]
i = 0
while i < len(fruits):
    if fruits[i] == "durian":
        fruits.pop(i)
    else:
        i += 1
print(fruits)




