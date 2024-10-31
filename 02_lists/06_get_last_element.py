"""Problem: Get Last Element
____________________________
Description: Fill out the function get_last_element(lst) which takes in a list lst as a parameter
and prints the last element in the list. 
The list is guaranteed to be non-empty, but there are no guarantees on its length.
"""
def take_list():
    user_list = []
    while True:
        user_input = str(input("Enter the element of the list and enter ! to end the list: "))
        if user_input == "!":
            break
        user_list.append(user_input)  
    return user_list

def get_last_element(lst):
    return lst[-1]

def main():
    user_list = take_list()
    print(user_list)
    last_element_of_list = get_last_element(user_list)
    print(last_element_of_list)

if __name__ == '__main__':
    main()