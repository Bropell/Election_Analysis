# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = str(input("Make your Choice: (r)ock, (p)aper, (s)cissors? "))

# Run Conditionals

if (user_choice == "r") and (computer_choice == "p"):

    print("You have lost")

elif (user_choice == "r") and (computer_choice == "s"):

    print("You have won")

elif (user_choice == "p") and (computer_choice == "r"):

    print("You have won")

elif (user_choice == "p") and (computer_choice == "s"):

    print("You have lost")

elif (user_choice == "s") and (computer_choice == "r"):

    print("You have lost")

elif (user_choice == "s") and (computer_choice == "p"):

    print("You have won")

elif user_choice == computer_choice:

    print("You have tied")

else:

    print("Enter a valid option")

print(f"You have chosen {user_choice}!")
print(f"The compter has chosen {computer_choice}!")
