""" Program: add2numbers
--------------------
Another python program to get some practice with
variables.  This program asks the user for two
integers and prints their sum.
"""
def main():
    print("This program adds two numbers.")
    num1 : str = input("Please enter your first number: ")
    num1 : int = int(num1)
    num2 : str = input("Please enter your second number: ")
    num2 : int = int(num2)
    add : int = num1 + num2
    print(f"The sum of the two numbers is : {add} ")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()