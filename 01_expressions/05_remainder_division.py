"""Problem: Remainder & Division 
________________________________
Description: Ask the user for two numbers, one at a time, 
and then print the result of dividing the first number by the second and
 also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):
Please enter an integer to be divided: 5
Please enter an integer to divide by: 3
The result of this division is 1 with a remainder of 2
"""
def divison(dividend, divisor):
    result = dividend // divisor
    return result

def remainder (dividend, divisor):
    result = dividend % divisor

def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input ("Please enter an integer to divide by: "))
    result_of_divion = divison(dividend, divisor)
    remainder_result = remainder(dividend, divisor)
    print(f"The result of this division is {result_of_divion} with a remainder of {remainder_result}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main() 
