# Question 1: Write a function to print “hello_USERNAME!” USERNAME is the input of the function.

def hello_name(user_name):
    """print a simple username"""
    name = input("Enter USERNAME: ")
    print("hello_" + name)

hello_name('arthur')

# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    """Print odd numbers in range 1-100"""
    for number in range(1, 101, 2):
            print(number, end =" ")

first_odds()
        


# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """print max number of a given list"""
    max = a_list[0]
    for num in a_list:
        if num > max:
            max = num
    return max

a_list = [45, 99, 1, 2, 150]
max_num = max_num_in_list(a_list)
print('\nYour max number is: ', max_num) 

# Question 4: Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
     """Find out if year is a leap year"""
     if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
          return True
     else:
          return False

a_year = int(input("\nEnter a year: "))
print(is_leap_year(a_year))

# Question 5: Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
     """Check if the list is consectuive or not"""
     return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

numbers = [5, 6, 7, 8, 9, 10]
print(f'\n{is_consecutive(numbers)}')