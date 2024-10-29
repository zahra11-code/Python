"""Program : Square Number
___________________________
Ask the user for a number and print its square (the product of the number times itself).
Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4
4.0 squared is 16.0
"""

def main():
    print("This program will give the sqaure of the your given number")
    num : float = float (input("Enter a number: "))
    print(str(num) + " is squared " + str(num **2))

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()