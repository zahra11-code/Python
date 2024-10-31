MAX_LEN: int = 3


def shorten_list(lst: list):
    while len(lst) > MAX_LEN:
        last_element = lst.pop()
        print("excluded element: ",last_element)


def take_list():
    user_list = []
    while True:
        input_list = input(
            "Enter an element of the list. Press Enter without typing to end: "
        )
        if input_list == "":
            break
        user_list.append(input_list)
    return user_list


def main():
    new_list = take_list()
    print("Original list:", new_list)
    shorten_list(new_list)
    print("Shortened list:", new_list)


if __name__ == "__main__":
    main()