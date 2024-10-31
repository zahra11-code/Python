"""This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 
Enter a number: 4 
Enter a number: 3 Enter a number: 6 
Enter a number: 4 Enter a number: 3 
Enter a number: 12
 Enter a number: 3
3 appears 3 times. 
4 appears 2 times. 
6 appears 1 times. 
12 appears 1 times.
"""

def take_list():
  num_list :list[int] = []
  for i in range(5):
        num = input("Please enter 5 numbers. After entering each number press the Enter key! ")
        num_list.append(int(num))

  return num_list

def count_num(lst):
  count = {}
  for num in lst:
    if num not in count:
      count[num] = 1
    else:
      count[num] += 1
  return count

def print_count(count):
  for num in count:
    print(f"{num} apperas {count[num]} times")
def main():
  new_list = take_list()
  print(new_list)      
  counting_numbers = count_num(new_list)  
  print(counting_numbers) 
  print_count(counting_numbers)

if __name__ == '__main__':
  main() 

     