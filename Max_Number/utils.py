
# Find max number in a list function
def find_max(numbers):
    """ Find the max number in a list """

    # numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
    answer = numbers[0]

    for num in numbers:
        if num > answer:
            answer = num

    return answer
