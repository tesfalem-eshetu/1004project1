import random

computer_guess = random.randint(1, 10)
number_of_incorrect_attempts = 0
print(computer_guess)
human_response = input("What do you think about my guess: ")
valid_response_list = ["correct", "too big", "too small"]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low = 0
high = len(arr) - 1

while number_of_incorrect_attempts < 4:
    while human_response not in valid_response_list:
        human_response = input("please input proper key word such as too big, too small, and correct : ")

    if human_response == "correct":
        print("congrats to me ; I guessed correctly")
        break
    else:
        number_of_incorrect_attempts += 1

        if human_response == "too big":
            high = arr.index(computer_guess)-1
            mid = (high + low) // 2
            computer_guess = arr[mid]
            print(computer_guess)
            human_response = input("What do you think about my guess: ")

        elif human_response == "too small":
            low = arr.index(computer_guess)+1
            mid = (high + low) // 2
            computer_guess = arr[mid]
            print(computer_guess)
            human_response = input("What do you think about my guess: ")

if human_response != "correct":
    print("computer loses")





