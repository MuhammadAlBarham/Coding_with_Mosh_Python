
numbers = [5, 1, 3, 2, 3, 7, 3, 4, 3, 5, 6, 5, 5, 5, 6, 7, 5]
numbers1 = numbers.copy()

i = 0
for num in numbers:
    j = i + 1
    while (j < len(numbers)):
        if num == numbers[j]:
            numbers.pop(j)
            continue
        j += 1
    i += 1

print(numbers)

uniques = []

for num in numbers1:
    if num not in uniques:
        uniques.append(num)

print(uniques)
