"""
Problem: Pythagorean Theorem
____________________________
Description: Write a program that asks the user for the lengths of the two perpendicular sides of
a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean
theorem!
The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras,
is a fundamental relation in geometry. It states that in a right triangle,
the square of the hypotenuse is equal to the sum of the square of the other two sides.
For instance, let's consider a right triangle ABC, with the right angle located at C.
According to the Pythagorean theorem:

BC ** 2 = AB ** 2 + AC ** 2

Your code should read in the lengths of the sides AB and AC, 
and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.
Here's a sample run of the program (user input is in bold italics):

Enter the length of AB: 3

Enter the length of AC: 4

The length of BC (the hypotenuse) is: 5.0
"""
from math import sqrt
def pythagoream_theorum(first_perpendicualr_side, second_perpendicualar_side):
    hypotenuse = (first_perpendicualr_side ** 2) + (second_perpendicualar_side ** 2 )
    return sqrt(hypotenuse)
    
def main():
    print("Find the length of hypotenuse side!")
    first_perpendicualr_side = float(input("Enter the length of AB: "))
    second_perpendicual_side = float(input("Enter the length of AC: "))
    hypotenuse = pythagoream_theorum(first_perpendicualr_side , second_perpendicual_side)
    print(f"The length of BC (the hypotenuse) is: {hypotenuse}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()