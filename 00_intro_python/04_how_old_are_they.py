"""Program: how old are they
____________________________
Description: a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.
"""
def main():
    friends = {"Anton" : 21, "Beth": 0, "Chen": 0, "Drew" : 0, "Ethan" : 0}
    friends["Beth"] = friends["Anton"] + 6
    friends["Chen"] = friends["Beth"] + 20
    friends["Drew"] = friends["Chen"] + friends["Anton"]
    friends["Ethan"] = friends["Chen"]

    for name, age in friends.items():
        print(f"{name} is {age}")

if __name__ == '__main__':
    main()
    