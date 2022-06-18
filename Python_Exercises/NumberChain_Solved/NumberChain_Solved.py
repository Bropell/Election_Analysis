# Initial variable to track game play
user_play = "y"

chain_start = 0


# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    numbers_to_loop = int(input("How many numbers would you like to loop through? "))

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    
    for i in range(chain_start,(chain_start + numbers_to_loop)):

        # Print each number in the range
       
       print(i)
    
    chain_start = chain_start + numbers_to_loop
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")

