# Password Generator 

import random

while True:

    try:
        alpha = "abcdefghijklmnopqrstuvwxyz"    # This variable stores alphabets
        
        cap_alpha = alpha.upper()               # This variable stores alphabets in upper case
        
        numbers = "0123456789"                  # This variable stores numbers in string data type 
        
        special_char = "!@#$%^&*()_+-=/*-+|[]{;:,./<>?}''"""        # This variable stores special characters
        
        combine = alpha + cap_alpha + numbers + special_char        # This variables combines all of the above variable 

        user_input = int(input("Enter a number to generate password: "))    # This takes input from the user and generates password length

        def conditions(user_input):
            """This function checks the conditions and returns output accordingly"""
        if user_input >= 6:     # Condition if user_input is equal to 6 or greater than 6
            
            password = ''.join(random.sample(combine, user_input))
            print(f"Your password is: {password}")      # Output
        
        else:
            
            print("Please enter greater than 5 to generate password")   # Will not generate password because user_input is less than 6

        conditions(user_input)        

        choice = input("Do you want to regenerate password?(y/n): ")    # It asks user to generate password again?

        if choice == "n" or choice == "n".upper():  # If n or N, it will exit the loop
            break

    except ValueError:      # This will throw error if, user does not write number.
        print("Please enter valid input, (please enter a number greater than 5)")   
