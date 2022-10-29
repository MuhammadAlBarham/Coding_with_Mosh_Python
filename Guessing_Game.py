secret_number = 9
guess_number = 0

while (guess_number < 3):
    number = int(input("Guess a number between 0 and 9: 10"))
    guess_number += 1
    if number == secret_number:
        print("You won!")
        break
else:
    print('Sorry, you failed!')
