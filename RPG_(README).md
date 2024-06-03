# Random Password Generator 

## Introduction

This Python script generates a random password based on user-defined length. It also handles errors.

## Features

1. **Import Library**: Utilizes the `random` module to generate random passwords.
2. **User-Defined Length**: Generates passwords according to the length specified by the user.
3. **Security**: Ensures the password length is greater than 5 for better security.
4. **f-string**: Uses f-strings to make the code cleaner and easier to maintain.

## How to Use 

1. **Run the Program**: Execute the script.
2. **Enter Input**: Enter the length of the password (a number greater than 5) to generate the password.
3. **View Result**: The program will display the generated password.
4. **Continue or Exit**: You will be given a choice if you wish to continue. Enter 'y' to continue or 'n' to stop.

## Code Explanation

1. The script uses a `while True` loop that runs continuously, prompting the user for input.
2. Inside the loop, the script uses a `try-except` block to handle any `ValueError` exceptions that may occur when the user enters invalid input.
3. The `alpha`, `cap_alpha`, `numbers`, and `special_char` variables store alphabets, capital letters, numbers, and special characters in string format.
4. The `combine` variable stores all of the above variables.
5. The `user_input` variable asks the user to "Enter a number to generate password." It generates a password of the specified length.
6. The `condition` function checks the user input and prints the output accordingly.
7. Then the user is asked, "Do you want to regenerate the password? (y/n):" to determine whether they want to continue or exit the program.
8. If the user presses 'n', the `break` statement is executed; otherwise, the script runs again.
