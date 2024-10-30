"""Problem: Write a function that takes a list of numbers and returns the sum of those numbers. """
def list_of_numbers():
    num_list :list[int] = []
    for i in range(1 , 6):
        num = input("Please enter 5 numbers. After entering each number press the Enter key! ")
        num_list.append(int(num))
    
    return num_list

def add_list_of_numbers():
    new_list : int = list_of_numbers()
    total : int = sum(new_list)
    return total



def main():
    sum_of_list = add_list_of_numbers()
    print(f"The sum of the numbers entered is eqaul to {sum_of_list}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()