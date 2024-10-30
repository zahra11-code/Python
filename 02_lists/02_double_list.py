"""Problem: Write a program that doubles each element in a list of numbers.
For example, if you start with this list:
numbers = [1, 2, 3, 4]
You should end with this list:
numbers = [2, 4, 6, 8]"""

def list_of_numbers():
    num_list :list[int] = []
    for i in range(1 , 6):
        num = input("Please enter 5 numbers. After entering each number press the Enter key! ")
        num_list.append(int(num))
    
    return num_list

def double_the_list():
    new_list: list[int] = list_of_numbers()
    double_list : list[int] = []
    for num in new_list:
        double_number = num * 2
        double_list.append(double_number)

    return double_list  


def main():
    double_list = double_the_list()
    print(double_list)

     



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()