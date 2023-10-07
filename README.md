The programs you submit in individual assignments must be your own work! You are, however, welcome to discuss the problem in general terms with other students as long as you don't discuss or exchange your code. Please review the academic honesty policy for this course (at the end of the syllabus page).

Do not use Python modules other than those explicitly mentioned. 

Please upload the following two files to Courseworks:

part1.py
part2.py

Important: If you re-submit your assignment, you need to re-upload both files, even if you changed just one of them. Otherwise, any files you uploaded previously will be lost. Courseworks will automatically append a suffix, for example, part1-2.py, when you resubmit to keep track of different versions. That's okay and not a cause for concern.

Before starting to program, make sure to plan out your algorithms (maybe on paper).

Part 1 - Guessing Game (50 pts)
In this problem you will implement a simple guessing game.

First, the program should choose a secret number x between 1 and 10 (inclusive, i.e., 1 <= x <= 10). Use the randint function in the randomLinks to an external site. module (random.randint()) to pick a random number.

Then the program should prompt the user to type in a number. Make sure to convert the input into an int.

If the user guesses x correctly, the program should print a message and terminate. Otherwise, the program should print a hint and then ask the user for another guess:

if the difference between x and the guess is greater than 5, the program prints ‘not even close’;
if the difference between x and the guess is between 2 and 5 (inclusive), the program prints ‘close’;
if the difference between x and the guess is less than 2, the program prints ‘almost there’.
The program should repeatedly ask the user for another input until the user guesses correctly or until there were five incorrect guesses. Use a loop to ask for guesses and print hints repeatedly. The program should keep track of the number of guesses. If the user cannot guess x in their fifth guess, the program informs them that the game is lost and quits.

Submit your guessing game program in one file called part1.py.   

Part 2 - Inverse Guessing Game (50 pts)

Let’s inverse the roles in the guessing game.

This time, the user chooses a secret number between 1 and 10 (in their mind -- they will not type the number) that the computer must guess. For this purpose, the computer suggests a number and the player indicates if it is: (1) too big, (2) too small, or (3) correct. The user's response should be read as input. If the number is correct, the program should print a confirmation and terminate. Otherwise, the computer should ask for another number repeatedly.

The computer has four attempts to guess the right number. Think about why the computer will always win the game.

The strategy for the computer to follow is similar to Binary Search (which will be covered in class). This is a requirement. The computer can start with a random initial guess, but should determine the next number based on the previous guess and the user's response, following a binary search strategy. Do not randomize subsequent guesses, only the first one.

Submit your inverse guessing game program in one file called part2.py.
