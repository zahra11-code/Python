"""Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

Here's a sample run (user input is in blue):

Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']"""

def tak_list():
    user_list = []
    while True:
        input_list =input("Enter the elment of the list. When you'll press enter without typing it will end: ")
        if input_list == "":
            break
        user_list.append(input_list)
    
    return user_list

def main():
    input_list = tak_list()
    print(input_list)
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()