numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]

ans = numbers[0]

for num in numbers:
    if num > ans:
        ans = num

print(ans)
