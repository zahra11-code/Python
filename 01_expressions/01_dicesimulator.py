"""Problem: Dice Simulator
_______________________
Description: Simulate rolling two dice, three times. Prints the results of each die roll. 
This program is used to show how variable scope works."""
import random
def roll_dice():
    die_1 = random.randint(1 , 6)
    die_2 = random.randint(1 , 6)
    return die_1, die_2


def main():
    print("This program is a dice simulator! :)")
    for i in range(1, 4):
        result = roll_dice()
        print(f"Roll {i}: {result[0]}, {result[1]} ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
