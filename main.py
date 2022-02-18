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