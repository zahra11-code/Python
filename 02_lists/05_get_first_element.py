"""Program: Get First Element
______________________________
Description: Fill out the function get_first_element(lst) which takes in a list lst as a parameter
and prints the first element in the list. The list is guaranteed to be non-empty. 
We've written some code for you which prompts the user to input the list one element at a time.
"""
def get_first_element(lst):
    print(lst[0])

def take_list():
  num_list :list[int] = []
  for i in range(5):
        num = input("Please enter 5 numbers. After entering each number press the Enter key! ")
        num_list.append(int(num))

  return num_list

def main():
    lst = take_list()
    get_first_element(lst)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()