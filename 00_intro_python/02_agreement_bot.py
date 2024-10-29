""" 
Program: AgreementBot
_______________

This program will promt the user for their favourite animal 
and then agree that it's my favourite animal too
"""

def main():
    favourite_animal : str = input("What's your favouritre animal? ") 
    print(f"My favorite animal is also {favourite_animal}!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()