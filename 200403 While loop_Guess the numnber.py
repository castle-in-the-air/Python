right_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the number is?'))
    guess_count += 1
    if guess == right_number:
        print("you win!")
        break
else:
    print("Sorry, you failed")