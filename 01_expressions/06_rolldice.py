"""Problem: Roll the dice
__________________________
Description: Simulate rolling two dice, and prints results of each roll as well as the total.
"""

from random import randint
NUM_SIDES :int = 6
def main():

    print(f"Dice have {NUM_SIDES} sides each.")
    die_1 = randint(1 , NUM_SIDES)
    die_2 = randint(1, NUM_SIDES)
    total : int = die_1 + die_2 
    
    print("First die:" , die_1)
    print("Second die:" , die_2)
    print("Total of roll dice: ", total)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()