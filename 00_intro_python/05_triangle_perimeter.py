"""Program: Triangle Perimeter
______________________________
Description: Prompt the user to enter the lengths of each side of a triangle and 
then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):
What is the length of side 1? 3
What is the length of side 2? 4
What is the length of side 3? 5.5
The perimeter of the triangle is 12.5
"""
def main():
    print("This program will print the perimeter of the triangle")
    first_side = input("What is the length of side 1? ")
    first_side : float = float(first_side)
    second_side = input("What is the length of side 2? ")
    second_side : float = float(second_side)
    third_side = input("What is the length of side 3? ")
    third_side : float = float(third_side)
    perimeter : float = first_side + second_side + third_side

    print(f"The perimeter of the triangle is {perimeter}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()