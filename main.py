import random

'''
Useful built-in functions
'''


'''
Methods to check a string value that returns a True or False Boolean value:

    isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
    isdigit() -- Returns True if all characters are the numbers 0-9.
    islower() -- Returns True if all cased characters are lowercase letters.
    isupper() -- Return True if all cased characters are uppercase letters.
    isspace() -- Return True if all characters are whitespace.
    startswith(x) -- Return True if the string starts with x.
    endswith(x) -- Return True if the string ends with x.

'''
'''
Methods to create new strings:

    capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
    lower() -- Returns a copy of the string with all characters lowercased.
    upper() -- Returns a copy of the string with all characters uppercased.
    strip() -- Returns a copy of the string with leading and trailing whitespace removed.
    title() -- Returns a copy of the string as a title, with first letters of words capitalized.

'''

my_list = []
i = 0
val = 'apple'
phrase = 'The quick brown fox jumps over the lazy dog'
start = 0
end = len(my_list)


# Get a new list containing some of another list's elements.
my_list[start:end]

# create a copy of a list using slice notation with no start or end indices
your_list = my_list[:]

# accepts a single iterable object argument, such as a string, list, or tuple, and returns a new list object. Ex: list('abc') creates a new list with the elements ['a', 'b', 'c'].
new_list = list('abcd')

#  splits a string into a list of tokens. Each token is a substring that forms a part of a larger string. Default is whitespace
words = phrase.split()

# join a list of strings together to create a single string. ex: 'seperator'.join(list)
second_phrase = ' '.join(words)

# Returns a copy of the string with all occurrences of the substring old replaced by the string new
val = val.replace('apple', 'orange')

# Returns the index of the first occurrence of item x in the string, else returns -1. find(x, start, end), rfind() for reverse search
char_index = val.find('n')

# Returns the number of times x occurs in the string
char_count = val.count('o')

# converts an integer into a character
chr(10)

# converts a character into an integer
ord('a')

# returns the number of elements in a sequence
len(val)

# find the element in list with the smallest value
min(my_list)

# find the element in list with the largest value
max(my_list)

# find the sum of all elements of a list (numbers only)
sum(my_list)

# True if every element in list is True (!= 0), or if the list is empty.
all(my_list)

# True if any element in the list is True.
any(my_list)

# reverse a list
reversed(my_list)

# return a random number arguments are minimum value and maximum value (must import random)
random_num = random.randint(0, 9)

# return a range of numbers where x is the starting value up to y (not included). z is the increment amount range(x, y, z) range(x) will return 0 - x
range(0, 10, 1)

# enumerate() returns the index and value in a list 
for (index, value) in enumerate(my_list):
    print(index, value)

'''
Useful built-in methods
'''
# add elements to a list
my_list.append(val)

# remove item at index i (default last)
my_list.pop(i)

# remove first element whos value is x Ex: .remove('apple')
my_list.remove(val)

# find the index of the first element in list whose value matches val
my_list.index(val)

# count the number of occurrences of the value val in list
my_list.count(val)

# sort a list
my_list.sort()

# Add all items in [x] to list.
my_list.extend([1, 2, 3])

# Insert x into list before position i my_list.insert(i, x)
my_list.insert(1, 7)

# reverse a list in-place
my_list.reverse()

# create a list from running map(), map() takes a function and iterable as arguments and performs the function on every element in the iterable
user_input = input()
test_grades = list(map(int, user_input.split())) # list- creates list with result of map. map- uses int() to conver every item in user_input.split() to integer.

'''
list comprehension
'''
# iterates over a list, modifies each element, and returns a new list consisting of the modified elements. 
# new_list = [expression for loop_variable_name in iterable]
our_list = [(i + 5) for i in my_list]

# A list comprehension can be extended with an optional conditional clause that causes the statement to return a list with only certain elements.
# new_list = [expression for name in iterable if condition]
our_list = [(i + 5) for i in my_list if (i % 2) == 0]

'''
Methods for sets (data type: set)
'''
# create set (empty set must used set())
num_set_1 = set()
num_set_2 = {1, 2, 3, 4}

#  places a new element into the set if the set does not contain an element with the provided value
num_set_1.add('1')

# remove a provided value from a set
num_set_2.remove('3')

# remove a random element from a set
num_set_2.pop()

# remove all elements from a set
num_set_1.clear()

# returns a new set containing only the elements in common between set and all provided sets
num_set_1.intersection(num_set_2)

# returns a new set containing all of the unique elements in all sets
num_set_1.union(num_set_2)

# returns a set containing only the elements of set that are not found in any of the provided sets
num_set_1.difference(num_set_2)

# returns a set containing only elements that appear in exactly one of set_a or set_b
num_set_1.symmetric_difference(num_set_2)

'''
Dictionaries (uses key/value pairs, access with key NOT index) (data type: mapping)
'''
# create a dictionary (empty)
pets = {}

# add entry to dictionary (key will mutated if already in dictionary)
pets['Tom'] = 'cat'
pets['Jerry'] = 'mouse'
pets['Spike'] = 'dog'

# remove entry from dictionary
del pets['Spike'] 

'''
program that takes age, weight, heart rate, and minutes of exercise as input,
then returns number of calories burned
'''
# user input
age = int(input('Age:\n> '))
weight = int(input('Weight:\n> '))
heart_rate = int(input('Heart rate:\n> '))
minutes = int(input('Minutes of exercise:\n> '))

# calculate calories burned
calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * minutes / 8.368

# output results with 2 decimal places
print(f'Calories: {calories:.2f} calories')

'''
program that takes number of quarters, dimes, nickels, and pennies as input,
and outputs total amount of money
'''
# user input
quarters = int(input('Quarters:\n> ')) * 0.25
dimes = int(input('Dimes:\n> ')) * 0.10
nickels = int(input('Nickels:\n> ')) * 0.05
pennies = int(input('Pennies:\n> ')) * 0.01

# process input
total = quarters + dimes + nickels + pennies

# output results with 2 decimal places
print(f'Amount: ${total:.2f}')

'''
program that calculates the half-life of caffeine
'''
# get input and convert to float
caffeine_mg = float(input())

# calculate half-life after 6, 12, and 24 hours
half_life_6 = caffeine_mg * (1/2)
half_life_12 = half_life_6 * (1/2)
half_life_24 = (half_life_12 * (1/2)) * (1/2)

# output results with special formatting (.2f is for two decimal places)
print(f'After 6 hours: {half_life_6:.2f} mg')
print(f'After 12 hours: {half_life_12:.2f} mg')
print(f'After 24 hours: {half_life_24:.2f} mg')

''' Given two integers that represent par and the number of strokes used,
    write a program that prints the appropriate score name. Print "Error" if par is not 3, 4, or 5 '''
# get input
par = int(input())
strokes = int(input())

# tuple of valid pars
valid_scores = (3, 4, 5)

# validate par and print appropriate output
if par in valid_scores:
    if (strokes - par == -2):
        print('Eagle')
    elif (strokes - par == -1):
        print('Birdie')
    elif (strokes - par == 0):
        print('Par')
    elif (strokes - par == 1):
        print('Bogey')
else:
    print('Error')

'''
Write a program that takes a date as input and outputs the date's 
season in the northern hemisphere. The input is a string to represent 
the month and an int to represent the day. In addition, check if the 
string and int are valid (an actual month and day). 
'''
input_month = input()
input_day = int(input())

months = ('January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October',
          'November', 'December')
          
months30 = ('April', 'June', 'September', 'November')

          
valid = ''

spring = ('March', 'April', 'May', 'June')
summer = ('June', 'July', 'August', 'September')
autumn = ('September', 'October', 'November', 'December')
winter = ('December', 'January', 'February', 'March')

message = ''

if (input_month in months) and ((input_day < 32) and (input_day > 0)):
    if ((input_month in months30) and (input_day > 30)) or ((input_month == 'February') and (input_day > 29)):
        valid = False
    else:
        valid = True
else:
    valid = False
    
    
if valid:
    if input_month in spring:
        message = 'Spring'
        if (input_month != 'March') and (input_month != 'June'):
            print(message)
        elif input_month == 'March':
            if (input_day >= 20) and (input_day <= 31):
                print(message)
        elif input_month == 'June':
            if (input_day >= 1) and (input_day <= 20):
                print(message)
        
            
    if input_month in summer:
        message = 'Summer'
        if (input_month != 'June') and (input_month != 'September'):
            print(message)
        elif input_month == 'June':
            if (input_day >= 21) and (input_day <= 30):
                print(message)
        elif input_month == 'September':
            if (input_day >= 1) and (input_day <= 21):
                print(message)
        
            
    if input_month in autumn:
        message = 'Autumn'
        if (input_month != 'September') and (input_month != 'December'):
            print(message)
        elif input_month == 'September':
            if (input_day >= 22) and (input_day <= 30):
                print(message)
        elif input_month == 'December':
            if (input_day >= 1) and (input_day <= 20):
                print(message)
        
            
    if input_month in winter:
        message = 'Winter'
        if (input_month != 'December') and (input_month != 'March'):
            print(message)
        elif input_month == 'December':
            if (input_day >= 21) and (input_day <= 31):
                print(message)
        elif input_month == 'March':
            if (input_day >= 1) and (input_day <= 19):
                print(message)
        
        
if not valid:
    print('Invalid')

'''
Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, 
and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the 
primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90. 
Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.
Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what 
primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west. 
'''
highway_number = int(input())

# declare variables
valid = False
num1 = 0
temp = 0
num2 = 0
highway_type = ''
direction = ''
service = ''

# validate input
if (highway_number > 99) and (highway_number < 1000):
    num1 = highway_number % 10
    temp = highway_number // 10
    num2 = temp % 10
   
if (highway_number > 0) and (highway_number < 100):
    valid = True

if (num1 + num2 != 0):
    valid = True
    if num2 == 0:
        service = num1
    else:
        service = str(num2) + str(num1)
# update variables   
if (highway_number > 0) and (highway_number < 100):
    highway_type = 'primary'
else:
    highway_type = 'auxiliary'
    
if highway_number % 2 == 0:
    direction = 'east/west'
else:
    direction = 'north/south'

# output
if valid:
    if (highway_type == 'auxiliary'):
        print(f'I-{highway_number} is {highway_type}, serving I-{service}, going {direction}.')
    elif (highway_type == 'primary'):
        print(f'I-{highway_number} is {highway_type}, going {direction}.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')
    

# loop over a dictionary
contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input()
new_email = input()
contact_emails[new_contact] = new_email

for contact in contact_emails:
    print(f'{contact_emails[contact]} is {contact}')


'''
Given num_rows and num_cols, print a list of all seats in a theater. 
Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat.
Sample output with inputs: 2 3

1A 1B 1C 2A 2B 2C 

'''
num_rows = int(input())
num_cols = int(input())

letter = ''

for i in range(num_rows):
    letter = 'A' # update variable outside inner loop so it starts at 'A' each time
    for j in range(num_cols):
        print(f'{i + 1}{letter}', end=' ')
        letter = chr(ord(letter) + 1) # converts to number than back to character adding 1 inbetween to get next character over

print()


'''
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) 
and the user must repeat the sequence. Create a for loop that compares each character of the 
two strings. For each matching character, add one point to user_score. Upon a mismatch, end the loop.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
User score: 4
'''

user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in range(10):
    if (simon_pattern[i] == user_pattern[i]):
        user_score += 1
    else:
        break

print('User score:', user_score)


'''
Write a program that takes in a line of text as input, and outputs that line 
of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" 
for the line of text.
'''

phrase = input()

exit_strings = ('Done', 'done', 'd')

valid = True

while valid:
    for i in reversed(phrase): # iterate over the reversed input
        print(i, end='')
        
    print() # put a new line between phrases
    phrase = input()
    if phrase in exit_strings: # check if the new input is an exit statement
        valid = False


'''
Write a program that reads a list of integers into a list as long as the integers 
are greater than zero, then outputs the smallest and largest integers in the list.
'''

num = int(input())

max_num = num
min_num = num
user_nums = []

# fill list with input until negative number
while num > 0:
    user_nums.append(num)
    num = int(input())

# find largest number
for i in range(len(user_nums)):
    if user_nums[i] > max_num:
        max_num = user_nums[i]

# find smallest number
for i in range(len(user_nums)):
    if user_nums[i] < min_num:
        min_num = user_nums[i]

# output min and max      
print(f'{min_num} and {max_num}')


'''
Many user-created passwords are simple and easy to guess. Write a program 
that takes a simple password and makes it stronger by replacing characters 
using the key below, and by appending "!" to the end of the input string.
note: strings are immutable, must concat using +=
'''

word = input()
password = ''

# dictionary of characters that should be converted
new_characters = {'i': '1', 
                  'a': '@', 
                  'm': 'M', 
                  'B': '8', 
                  's': '$'}


for i in range(len(word)): # loops through string input
    if word[i] in new_characters: # checks to see if current character is in dictionary
        password += new_characters[word[i]] # access dictionary value with key of current character from word
    else:
        password += word[i]
else:                         # this line runs when the entire loop has completed
    password += '!'

print(password)

'''
Define a function named swap_values that takes four integers as parameters and swaps the 
first with the second, and the third with the fourth values. Then write a main program that 
reads four integers from input, calls function swap_values() to swap the values, and prints 
the swapped values on a single line separated with spaces.
'''

def swap_values(user_val1, user_val2, user_val3, user_val4):
   
    temp = user_val1
    user_val1 = user_val2
    user_val2 = temp
    temp = user_val3
    user_val3 = user_val4
    user_val4 = temp
    # returns a tuple (allows returning multiple variables)
    return (user_val1, user_val2, user_val3, user_val4)


val1 = int(input())
val2 = int(input())
val3 = int(input())
val4 = int(input())

# tuple unpacking (assigns multiple values at once by position)
(val1, val2, val3, val4) = swap_values(val1, val2, val3, val4)
print(f'{val1} {val2} {val3} {val4}')

'''
Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's 
representing the integer in binary. The program must define and call the following two functions. 
Define a function named int_to_reverse_binary() that takes an integer as a parameter and returns a 
string of 1's and 0's representing the integer in binary (in reverse). Define a function named string_reverse() 
that takes an input string as a parameter and returns a string representing the input string in reverse.
'''
def int_to_reverse_binary(integer_value):
    reverse_binary = []
    while integer_value > 0:
        reverse_binary.append(str(integer_value % 2))
        integer_value = integer_value // 2
    return ''.join(reverse_binary)
    
def string_reverse(input_string):
    return input_string[::-1] # easy way to reverse string ('slice' [begin:end:step] if begin and end omitted, 0 - end implied)

user_val = int(input())
print(string_reverse(int_to_reverse_binary(user_val)))


'''
Define a function called exact_change that takes the total change amount in cents and calculates 
the change using the fewest coins. The coin types are pennies, nickels, dimes, and quarters. Then write 
a main program that reads the total change amount as an integer input, calls exact_change(), and outputs 
the change, one coin type per line. Use singular and plural coin names as appropriate, 
like 1 penny vs. 2 pennies. Output "no change" if the input is 0 or less.
'''

def exact_change(coins):
  
  quarters = coins // 25 # divides and removes remainder
  coins = coins % 25 # uses modulo to get remaing coin amount
  
  dimes = coins // 10
  coins = coins % 10
  
  nickels = coins // 5
  coins = coins % 5

  pennies = coins

  return (pennies, nickels, dimes, quarters)

input_val = int(input())    
num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
    
if input_val > 0:
    if num_pennies > 0:
        if num_pennies > 1:
            print(f'{num_pennies} pennies')
        else:
            print(f'{num_pennies} penny')
            
    if num_nickels > 0:
        if num_nickels > 1:
            print(f'{num_nickels} nickels')
        else:
            print(f'{num_nickels} nickel')
            
    if num_dimes > 0:
        if num_dimes > 1:
            print(f'{num_dimes} dimes')
        else:
            print(f'{num_dimes} dime')
            
    if num_quarters > 0:
        if num_quarters > 1:
            print(f'{num_quarters} quarters')
        else:
            print(f'{num_quarters} quarter')
else:
    print('no change')


'''
Many documents use a specific format for a person's name. Write a program whose input is:
firstName middleName lastName
and whose output is:
lastName, firstInitial.middleInitial
If the input has the form:
firstName lastName
the output is:
lastName, firstInitial. 
'''

full_name = input()

count = full_name.count(' ') # counts whitespace to tell if three names(2 spaces) or two(1 space)
name_arr = full_name.split()

name_arr.insert(0, name_arr[len(name_arr) -1]) # puts the last name in front
name_arr.pop() # removes duplicate lastname from end
name_arr[0] += ', ' # add comma and space for formatting

if (count == 2): # swaps out the name for just the first letter then adds a '.'
  name_arr[1] = name_arr[1][0] 
  name_arr[1] += '.'
  name_arr[2] = name_arr[2][0]
  name_arr[2] += '.'
elif (count == 1):
  name_arr[1] = name_arr[1][0]
  name_arr[1] += '.'
  
edited_name = ''.join(name_arr)
print(edited_name)

'''
Write a program whose input is a phrase and whose output 
is an acronym of the input. Append a period (.) after each 
letter in the acronym. If a word begins with a lower case 
letter, don't include that letter in the acronym. Assume the 
input has at least one upper case letter.
'''
phrase = input()

phrase_arr = phrase.split()
acronym_arr = [] # empty list to append to

for i in range(len(phrase_arr)):
    if (phrase_arr[i][0].isupper()): # check if the first letter is a capital
        acronym_arr.append(phrase_arr[i][0]) # appends if true
else:
    acronym_arr[-1] += '.' # adds a '.' to the last element (-1) after the final iteration
        
acronym = '.'.join(acronym_arr)

print(acronym)


'''
Write a program that takes in two strings and 
outputs the longest string. If they are the same 
length then output the second string.
'''

def find_longer(first_string, second_string):
    longer_string = None
    if len(first_string) > len(second_string):
        longer_string = first_string
    else:
        longer_string = second_string
        
    return longer_string


string1 = input()
string2 = input()


print(find_longer(string1,string2))


'''
Given a line of text as input, output the number of characters 
excluding spaces, periods, exclamation points, or commas.
'''

user_text = input().lower()

text_arr = user_text.split()
excluded_characters = [' ', '.','!',',']
count = 0



for i in range(len(text_arr)):
    for j in range(len(text_arr[i])):
        if text_arr[i][j] in excluded_characters:
            continue
        else:
            count += 1

print(count)

'''
Write a function max_magnitude() with three integer parameters 
that returns the largest magnitude value. Use the function in the 
main program that takes three integer inputs and outputs the largest 
magnitude value.
'''

def max_magnitude(user_val1, user_val2, user_val3):
    users = [user_val1, user_val2, user_val3]
    max_num = user_val1
    for num in users:
        if math.fabs(num) > math.fabs(user_val1):
            max_num = num
    
    return max_num
    
if __name__ == '__main__':
    
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(max_magnitude(num1, num2, num3))


'''
Print the two-dimensional list mult_table by row and column. 
On each line, each character is separated by a space. Hint: Use nested loops.

'''
user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

# convert to int <- for every number in the nested list <- for every element in lines (lines is a list of lists)
mult_table = [[int(num) for num in line.split()] for line in lines]

for row in mult_table:
    for cell in row:
        if (row.index(cell) != len(row) - 1): # if the element is not the last one, use the seperator ' | '
            print(cell, end=' | ')
        else:
            print(cell, end='')
    
    print() # create a new line between rows

'''
Complete the solution so that it reverses the string passed into it. 
'''
def solution(string):
    reversed = []
    i = len(string) - 1
    
    while i >= 0:
        reversed.append(string[i])
        i -= 1
        
    return ''.join(reversed)