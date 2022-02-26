'''
Useful built-in functions
'''
my_list = []
i = 0
val = 'apple'

# returns the number of elements in a sequence
len(val)

# find the element in list with the smallest value
min(my_list)

# find the element in list with the largest value
max(my_list)

# find the sum of all elements of a list (numbers only)
sum(my_list)

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
    

