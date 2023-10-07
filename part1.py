# imported to generate random number
import random

# assigned a number to be generated randomly
secret_number = random.randint(1, 10)

# feel free to uncomment it for testing purposes
# print(secret_number)

# will be uses to keep track of incorrect attempts made
number_of_incorrect_attempt = 0

# this loop will run until the user found the number or make 5 mistakes in a row ,which ever comes first
# used the absolute value function to check for the difference between guess number and secret number
while number_of_incorrect_attempt < 5:
    guess_number = int(input("Please enter your guess here ,from 1 to 10 :"))
    if guess_number == secret_number:
        print("Congrats, you guessed correctly, consider buying a lottery.")
        break
    else:
        number_of_incorrect_attempt += 1
        if abs(guess_number - secret_number) > 5:
            print("not even close")
        elif 2 <= abs(guess_number - secret_number) <= 5:
            print("close")
        elif abs(guess_number - secret_number) < 2:
            print("almost there")
# if the user doesn't make it by the fifth try the program will stop
if guess_number != secret_number:
    print("Game over secrete number was ", secret_number)


