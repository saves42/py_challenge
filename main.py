import array
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

'''
string formatting
'''
# 12 = minimum number of characters / > = alignment character for word (<left,>right,^center) / '-' = fill character when word does not meet min requirement
word = 'world'
print(f'{"hello":->12}{word:->12}') # prints -------hello-------world

'''
following code will print:

item           price    
------------------------
coffee          1.5     
donut           0.5     
energy drink    2.5     
sandwich        4.25 

'''
stock = { 
          'coffee': 1.50,
          'donut': .50,
          'energy drink': 2.50,
          'sandwich': 4.25
}

print(f'{"item":<12}{"price":^12}')
print('-' * 24)

for item, price in stock.items():
  print(f'{item:<12}{price:^12}')

#########################################################################################################

my_list = []
i = 0
val = 'apple'
phrase = 'The quick brown fox jumps over the lazy dog'
start = 0
end = len(my_list)
stride = 2 # increments by 2

# Get a new list containing some of another list's elements.
my_list[start:end:stride]

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
list comprehension example
'''

'''
Make a program that filters a list of strings and returns a list with only your 
friends name in it. If a name has exactly 4 letters in it, you can be sure 
that it has to be a friend of yours! Otherwise, you can be sure he's not...
'''

def friend(x):
    return [y for y in x if len(y)==4]

##########################################################################################################

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

#######################################################################################################

'''
Dictionaries (uses key/value pairs, access with key NOT index) (data type: mapping)
'''
# create a dictionary (empty)
pets = {}

# add entry to dictionary (key will mutated if already in dictionary)
pets['Tom'] = 'cat'
pets['Jerry'] = 'mouse'
pets['Spike'] = 'dog'

# dictionary methods
pets.items() # returns a view object that yields (key, value) tuples.
pets.keys() # returns a view object that yields dictionary keys.
pets.values() # returns a view object that yields dictionary values.

#########################################################################################################

'''
working with files
'''
# The open() built-in function requires a single argument that specifies the path to the file. 
# Ex: open('myfile.txt')
# The file.close() method closes the file, after which no more reads or writes to the file are allowed.
# The file.read() method returns the file contents as a string.
# The file.readlines() method returns a list of strings, where the first element is the contents 
# of the first line, the second element is the contents of the second line, and so on.
# The file.write() method writes a string argument to a file.
# The write() method accepts a string argument only. Integers and floating-point values must first be 
# converted using str(), as in f.write(str(5.75))
# When writing to a file, the mode of the file must be explicitly set in the open() function call. 
# A mode indicates how a file is opened, e.g., whether or not writing to the file is allowed, if existing 
# contents of the file are overwritten or appended, etc.
'''
Mode 	Description 	                                    Allow read?     Allow write?   Create missing file?     Overwrite file?
'r' 	Open the file for reading. 	                            Yes 	         No 	           No 	                   No

'w' 	Open the file for writing.               	            No 	             Yes 	           Yes	                   Yes
        If file does not exist then the file is created.
        Contents of an existing file are overwritten.

'a' 	Open the file for appending.     	                    No 	             Yes 	           Yes 	                   No
        If file does not exist then the file is created.        
        Writes are added to end of existing file contents.


Read mode 'r' opens a file for reading. If the file is missing, then an error will occur.
Write mode 'w' opens a file for writing. If the file is missing, then a new file is created. Contents of any existing file are overwritten.
Append mode 'a' opens a file for writing. If the file is missing, then a new file is created. Writes to the file are appended to the end of an existing file's contents.
Additionally, a programmer can add a '+' character to the end of a mode, like 'r+' and 'w+' to specify an update mode. Update modes allow for both reading and writing of a file at the same time.
'''

# Read file contents
print ('Reading in data....')
f = open('mydata.txt')
lines = f.readlines()
f.close()

# Iterate over each line
print('\nCalculating average....')
total = 0
for ln in lines:
    total += int(ln)

# Compute result
avg = total/len(lines)
print('Average value:', avg)

"""Echo the contents of a file."""
f = open('myfile.txt')

for line in f:
    print(line, end="")

f.close()

# os.path.join() example:
# path = os.path.join('subdir', 'bat_mobile.jpg')
# which will result in "subdir\\bat_mobile.jpg" on Windows and "subdir/bat_mobile.jpg" on Linux/Mac. 

# os.path.split(path) – Splits a path into a 2-tuple (head, tail), where tail is the last token in the 
# path string and head is everything else.

# os.path.exists(path) – Returns True if path exists, else returns False.

# os.path.isfile(path) – Returns True if path is an existing file, and false otherwise 
# (e.g., path is a directory).

# os.path.getsize(path) – Returns the size in bytes of path.

# The os.walk() function 'walks' a directory tree, visiting each subdirectory in the specified path. 
# The following example walks a user-specified year of the above directory tree.

import os

year = input('Enter year: ')
path = os.path.join('logs', year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)

# The os.walk() function is used as the iterable object in a for loop that yields a 3-tuple for each 
# iteration.2 The first item dirname contains the path to the current directory. The second item subdirs 
# is a list of all the subdirectories of the current directory. The third item files is a list of all the 
# files residing in the current directory. array programmer might use os.walk() when searching for 
# specific files within a directory tree, and the exact path is unknown. Another common task is to 
# filter files based on their file extensions (.pdf, .txt, etc.), which are a convention used to 
# indicate the type of data that a file holds.


'''
Output
Enter year:2009

logs\2009 contains subdirectories: ['April', 'January'] and the files: []
logs\2009\April contains subdirectories: ['1'] and the files: []
logs\2009\April\1 contains subdirectories: [] and the files: ['log.txt', 'words.doc']
logs\2009\January contains subdirectories: ['15', '21', '24'] and the files: []
logs\2009\January\15 contains subdirectories: [] and the files: ['log.txt']
logs\2009\January\21 contains subdirectories: [] and the files: ['log.txt', 'temp23.pdf']
logs\2009\January\24 contains subdirectories: [] and the files: ['presentation.ppt']
'''


# file path example

import os
import datetime

curr_day = datetime.date(1997, 8, 29)

num_days = 30
for i in range(num_days):
    year = str(curr_day.year)
    month = str(curr_day.month)
    day = str(curr_day.day)

    # Build path string using current OS path separator
    file_path = os.path.join('logs', year, month, day, 'log.txt')

    f = open(file_path, 'r')
    
    print(f'{file_path}: {f.read()}')
    f.close()

    curr_day = curr_day + datetime.timedelta(days=1)



'''
Write a program that first reads in the name of an input file, followed 
by two strings representing the lower and upper bounds of a search range. 
The file should be read using the file.readlines() method. The input file 
contains a list of alphabetical, ten-letter strings, each on a separate 
line. Your program should output all strings from the list that are within 
that range (inclusive of the bounds).
'''
path = input()

with open(path, 'r') as text:
    words = text.readlines()
    
lower_bound = input()
upper_bound = input()

    
for word in words:
    if (word.strip() >= lower_bound) and (word.strip() <= upper_bound):
        print(word.strip())



'''
Write a program that first reads in the name of an input file and then reads the 
file using the csv.reader() method. The file contains a list of words separated by commas. 
Your program should output the words and their frequencies 
(the number of times each word appears in the file) without any duplicates.
'''

import csv

path = input()
skip = []

with open(path, 'r') as csvfile:
    words = csv.reader(csvfile, delimiter=',')
    
    for row in words:
        for word in row:
            if word in skip:
                continue
            else:
                skip.append(word)
                print(f'{word} {row.count(word)}')

# A programmer can also use the csv module to write text into a csv file, using a writer object. 
# The writer object's writerow() and writerows methods can be used to write a list of strings into 
# the file as one or more rows. 

'''
Write a program that first reads in the name of an input file and then reads the input file 
using the file.readlines() method. The input file contains an unsorted list of number of seasons 
followed by the corresponding TV show. Your program should put the contents of the input file 
into a dictionary where the number of seasons are the keys, and a list of TV shows are the values 
(since multiple shows could have the same number of seasons). Sort the dictionary by key 
(least to greatest) and output the results to a file named output_keys.txt. Separate multiple 
TV shows associated with the same key with a semicolon (;), ordering by appearance in the 
input file. Next, sort the dictionary by values (alphabetical order), and output the results 
to a file named output_titles.txt.
'''


file = input()
movies = {}
reference_key = ''
i = 0
movie_list = []

with open(file, 'r') as moviefile:
    for entry in moviefile.readlines():
        if i % 2 == 0:
            
            if int(entry.strip()) in movies:
                reference_key = int(entry.strip())
            else:
                movies[int(entry.strip())] = []
                reference_key = int(entry.strip())
            
        else:
            movies[reference_key].append(entry.strip())
        
        i += 1 

with open('output_keys.txt', 'w') as output_keys:
    
    for key in sorted(movies.keys()):
            output_keys.write(f'{key}: ')
            for movie in movies[key]:
                if movies[key].index(movie) == len(movies[key]) - 1:
                    output_keys.write(f'{movie}\n')
                else:
                    output_keys.write(f'{movie}; ')

for key in movies:
        for movie in movies[key]:
            movie_list.append(movie)

with open('output_titles.txt', 'w') as output_titles:
    for movie in sorted(movie_list):
        output_titles.write(f'{movie}\n')
        
        

'''
Write a program that reads the name of a text file containing a 
list of photo file names. The program then reads the photo file names 
from the text file, replaces the "_photo.jpg" portion of the file 
names with "_info.txt", and outputs the modified file names. 
'''

file = input()
extension = '_info.txt'

with open(file, 'r') as photo_file:
    for entry in photo_file.readlines():
        print(f'{entry.strip().split("_").pop(0)}{extension}')



'''
Write a program that reads movie data from a CSV (comma separated values) file and output the data in a 
formatted table. The program first reads the name of the CSV file from the user. The program then reads 
the CSV file and outputs the contents according to the following requirements:

    Each row contains the title, rating, and all showtimes of a unique movie.
    A space is placed before and after each vertical separator ('|') in each row.
    Column 1 displays the movie titles and is left justified with a minimum of 44 characters.
    If the movie title has more than 44 characters, output the first 44 characters only.
    Column 2 displays the movie ratings and is right justified with a minimum of 5 characters.
    Column 3 displays all the showtimes of the same movie, separated by a space.

Each row of the CSV file contains the showtime, title, and rating of a movie. Assume data of the same 
movie are grouped in consecutive rows. 

If the input of the program is: movies.csv

and the contents of movies.csv are:

16:40,Wonders of the World,G
20:00,Wonders of the World,G
19:00,Journey to Space,PG-13
12:45,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
15:00,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
19:30,Buffalo Bill And The Indians or Sitting Bull's History Lesson,PG
10:00,Adventure of Lewis and Clark,PG-13
14:30,Adventure of Lewis and Clark,PG-13
19:00,Halloween,R

the output of the program is:

Wonders of the World                         |     G | 16:40 20:00
Journey to Space                             | PG-13 | 19:00
Buffalo Bill And The Indians or Sitting Bull |    PG | 12:45 15:00 19:30
Adventure of Lewis and Clark                 | PG-13 | 10:00 14:30
Halloween                                    |     R | 19:00

'''

import csv

file = input()
movies = {}

with open(file, 'r') as csvfile:
    movie_data = csv.reader(csvfile)
    
    for line in movie_data:
        movies[line[1]] = {
            'rating': line[2].strip(),
            'times': []
            }
            
with open(file, 'r') as csvfile:
    movie_data = csv.reader(csvfile)            
    for line in movie_data:
        if line[0] in movies[line[1]]['times']:
            continue
        else:
            movies[line[1]]['times'].append(line[0])

for key in movies.keys():
    title = f'{key[:44]:<44}'
    rating = f"{movies[key]['rating']:>5}"
    times = ' '.join(movies[key]['times'])
    sep = f"{'|':^3}"
    print(f'{title}{sep}{rating}{sep}{times}')

#########################################################################################################

'''
Try/except example
'''

def get_age():
    age = int(input())
    if (age > 17) and (age < 76):
        return age
        
    else:
        raise ValueError('Invalid age.')

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * (70/100)
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print(f'Fat burning heart rate for a {age} year-old: {fat_burning_heart_rate(age)} bpm')
    except ValueError as err:
        print(err)
        print('Could not calculate heart rate info.')

def get_weight():
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        raise ValueError('Invalid weight.')
    return weight

def get_height():
    height = int(input('Enter height (in inches): '))
    if height <= 0:
        raise ValueError('Invalid height.')
    return height

user_input = ''
while user_input != 'q':
    try:
        weight = get_weight()
        height = get_height()

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")

'''
Custom exception example
-------------------------

class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value

my_num = int(input('Enter number: '))

if my_num < 0:
    raise LessThanZeroError('my_num must be greater than 0')
else:
    print('my_num:', my_num)

Good practice is to include "Error" at the end of a custom exception type's name, as in 
LessThanZeroError or MyError. Custom exception types are useful to track and handle the unique 
exceptions that might occur in a program's code. Many larger third-party and Python standard 
library modules use custom exception types.
'''

#########################################################################################################

'''
classes
'''
# __init__(self) method constructor used to initialize a class to a specific state
# Constructor parameters can have default values like any other function, using the name=value syntax.
# Arguments without default values are required, must come first, and must be in order.
# EX: __init__(self, age, name, salary=15.00)
# A class may also contain methods used internally that a user of the class need not access. 
# For example, consider if the RaceTime class contains a separate method _diff_time() used by print_time() 
# and print_pace() to find the total number of minutes to complete the race.
# Good practice is to prepend an underscore to methods only used internally by a class.
'''
Class customization is the process of defining how a class should behave for some common operations. 
Such operations might include printing, accessing attributes, or how instances of that class are 
compared to each other. To customize a class, a programmer implements instance methods with special 
method names that the Python interpreter recognizes

Normal printing

class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age


truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)

<__main__.Toy instance at 0xb74cb98c>

Customized printing

class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age

    def __str__(self):
        return (f'{self.name} costs only ${self.price:.2f}.'
                f' Not for children under {self.min_age}!')

truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)

'''

'''
Overloading

Class customization can redefine the functionality of built-in operators like 
<, >=, +, -, and * when used with class instances, a technique known as operator overloading. 

The below code shows overloading of the less-than (<) operator of the Time class by defining 
a method with the __lt__ special method name.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.hours}:{self.minutes}'

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

Rich comparison method 	Overloaded operator
---------------------------------------------
__lt__(self, other) 	less-than (<)
__le__(self, other) 	less-than or equal-to (<=)
__gt__(self, other) 	greater-than (>)
__ge__(self, other) 	greater-than or equal-to (>=)
__eq__(self, other) 	equal to (==)
__ne__(self, other) 	not-equal to (!=)

In the above program, the Time class contains a definition for the __lt__ method, 
which overloads the < operator. When the comparison t < min_time is evaluated, the __lt__ method 
is automatically called. The self parameter of __lt__ is bound to the left operand, t, and the other 
parameter is bound to the right operand, min_time. Returning True indicates that t is indeed less-than 
min_time, and returning False indicates that t equal-to or greater-than min_time. Methods like __lt__ 
above are known as rich comparison methods. The following table describes rich comparison methods 
and the corresponding relational operator that is overloaded. 

Numeric operators such as +, -, *, and / can be overloaded using class customization techniques. 
Thus, a user-defined class can be treated as a numeric type of object wherein instances 
of that class can be added together, 
multiplied, etc.

class Time24:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'

    def __gt__(self, other): 
        if self.hours > other.hours: 
            return True 
        else: 
            if self.hours == other.hours: 
                if self.minutes > other.minutes: 
                    return True 
        return False

    def __sub__(self, other):
        """ Calculate absolute distance between two times """
        if self > other:
            larger = self
            smaller = other
        else:
            larger = other
            smaller = self

        hrs = larger.hours - smaller.hours
        mins = larger.minutes - smaller.minutes
        if mins < 0:
            mins += 60
            hrs -=1

        # Check if times wrap to new day
        if hrs > 12:
            hrs = 24 - (hrs + 1)
            mins = 60 - mins

        # Return new Time24 instance 
        return Time24(hrs, mins)

t1 = input('Enter time1 (hours:minutes): ')
tokens = t1.split(':')
time1 = Time24(int(tokens[0]), int(tokens[1]))

t2 = input('Enter time2 (hours:minutes): ')
tokens = t2.split(':')
time2 = Time24(int(tokens[0]), int(tokens[1]))

print('Time difference:', time1 - time2)

Output:
Enter time1 (hours:minutes): 5:00
Enter time2 (hours:minutes): 3:30
Time difference: 01:30
...
Enter time1 (hours:minutes): 22:30
Enter time2 (hours:minutes): 2:40
Time difference: 04:10


Every operator in Python can be overloaded. The table below lists some of the most common methods. 
A full list is available at the bottom of the section.

Method 	                    Description
__add__(self, other) 	    Add (+)
__sub__(self, other) 	    Subtract (-)
__mul__(self, other) 	    Multiply (*)
__truediv__(self, other) 	Divide (/)
__floordiv__(self, other) 	Floored division (//)
__mod__(self, other) 	    Modulus (%)
__pow__(self, other) 	    Exponentiation (**)
__and__(self, other) 	    "and" logical operator
__or__(self, other) 	    "or" logical operator
__abs__(self)           	Absolute value (abs())
__int__(self) 	            Convert to integer (int())
__float__(self) 	        Convert to floating point (float())

The table above lists common operators such as addition, subtraction, multiplication, division, and so on.
Sometimes a class also needs to be able to handle being passed as arguments to built-in functions like
abs(), int(), float(), etc. Defining the methods like __abs__(), __int__(), and __float__() will 
automatically cause those methods to be called when an instance of that class is passed to the 
corresponding function. The methods should return an appropriate object for each method, i.e., an integer 
value for __int__() and a floating-point value for __float__().
'''

# class example
class Inventory:
  def __init__(self):
    self.stock = { 
          'coffee': 1.50,
          'donut': .50,
          'energy drink': 2.50,
          'sandwich': 4.25
}
  def add_menu_item(self, item, price):
    self.stock[item] = price

  
  def get_price(self, item):
    return f'The price of {item} is {self.stock[item]}'

  
  def get_total(self, items):
    total = 0

    for item in items:
      total += self.stock[item]

    return total

  
  def print_menu(self):
    print(f'{"item":<12}{"price":^12}')
    
    print('-' * 24)
    
    for item, price in self.stock.items():
      print(f'{item:<12}{price:^12}')

    print()


snacks = Inventory()

snacks.print_menu()

snacks.add_menu_item('ice cream', 1.25)

snacks.print_menu()

print(snacks.get_price('coffee'))

print(snacks.get_total(['coffee', 'donut', 'sandwich']))

'''
Inheritance
'''

# base class
class Item:
    def __init__(self):
        self.name = ''
        self.quantity = 0

# derived class (inherits Item class)
class Produce(Item):
    def __init__(self):
        Item.__init__(self) # call Item constructor
        self.expiration = ''


'''
A class can inherit from more than one base class, a concept known as multiple inheritance. The derived 
class inherits all of the class attributes and methods of every base class.

    # ...
class VampireBat(WingedAnimal, Mammal):  # Inherit from WingedAnimal, Mammal classes
    # ...

Mixins are classes that provide some additional behavior, by "mixin in" new methods, 
but are not themselves meant to be instantiated. 

class DrivingMixin(object):
    def drive(self, distance):
        # ...

    def change_tire(self):
        # ...

    def check_oil(self):
        # ...

class FlyingMixin(object):
    def fly(self, distance, altitude):
        # ...

    def roll(self):
        # ...

    def eject(self):
        # ...

class TransportMode(object):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def display(self):
        print(f'{self.name} can go {self.speed} mpg')

class SemiTruck(TransportMode, DrivingMixin):
    def __init__(self, name, speed, cargo):
        TransportMode.__init__(self, name, speed)
        self.cargo = cargo

    def go(self, distance):
        self.drive(distance)
        # ...

class FlyingCar(TransportMode, FlyingMixin, DrivingMixin):
    def __init__(self, name, speed, max_altitude):
        TransportMode.__init__(self, name, speed)
        self.max_altitude = max_altitude

    def go(self, distance):
        self.fly(distance / 2, self.max_altitude)
        # ...
        self.drive(distance / 2)

s = SemiTruck('MacTruck', 85, 'Frozen beans')
f = FlyingCar('Jetson35K', 325, 15000)

s.go(100)
f.go(100)

'''


# An attribute reference is resolved using a search procedure that first checks the instance's namespace, 
# then the classes' namespace, then the namespaces of any base classes. The search for an attribute 
# continues all the way up the inheritance tree, which is the hierarchy of classes from a derived class to 
# the final base class.

# A derived class may define a method having the same name as a method in the base class. Such a member 
# function overrides the method of the base class.
# A programmer will often want to extend, rather than replace, the base class method. The base class 
# method can be explicitly called at the start of the method, with the derived class then performing 
# additional operations: 
class Produce(Item):
    # ...
    def display(self):
        Item.display(self)
        print(f'  (Expires: {self.expiration})')
    # ...

#########################################################################################################


'''
Unit testing
'''

# Example

import unittest

# User-defined class
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius**2


# Class to test Circle
class TestCircle(unittest.TestCase):
    def test_compute_area(self):
        c = Circle(0)
        self.assertEqual(c.compute_area(), 0.0)

        c = Circle(5)
        self.assertEqual(c.compute_area(), 78.5)

    def test_will_fail(self):
        c = Circle(5)
        self.assertLess(c.compute_area(), 0)

if __name__ == "__main__":
    unittest.main()

'''
The program above implements a unit test for the Circle.compute_area() method. A new class TestCircle is 
defined that inherits from unittest.TestCase. Methods within the TestCircle class that begin with "test_" 
are the unit tests to be run. A unit test performs assertions to check if a computed value meets certain 
requirements. Above, self.assertEqual( c.compute_area(), 78.5 ) asserts that the result of 
c.compute_area() is equal to 78.5. If the assertion is not true, then an AssertionError will be raised 
and the current test will report as a failure. Executing the unittest.main() function begins the test 
process. After all tests have completed, a report is automatically printed.

Assertion methods

Method 	                    Checks that
assertEqual(a, b) 	        a == b
assertNotEqual(a,b) 	    a != b
assertTrue(x) 	            bool(x) is True
assertFalse(x) 	            bool(x) is False
assertIs(a, b) 	            a is b
assertIsNot(a,b) 	        a is not b
assertIsNone(x) 	        x is None
assertIsNotNone(x) 	        x is not None
assertIn(a, b) 	            a in b
assertNotIn(a, b) 	        a not in b
assertAlmostEqual(a, b) 	round(a - b, 7) == 0
assertGreater(a, b) 	    a > b
assertGreaterEqual(a, b) 	a >= b
assertLess(a, b) 	        a < b
assertLessEqual(a, b) 	    a <= b

'''


'''
--Use list() to convert view objects into lists to manipulate--

solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

sorted_distance_list = sorted(list_of_distances)
closest = sorted_distance_list[0]
next_closest = sorted_distance_list[1]

print(f'Closest planet is {closest:.4e}')
print(f'Second closest planet is {next_closest:.4e}')

'''
# iterate over dictionaries

for name, animal in pets: # using key/value pair
    print(f'{name} is a {animal}')

for name in pets.keys(): # using keys
    print(name)

for animal in pets.value(): # using value
    print(animal)


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
    # alternate solution -> return string[::-1] (slice method) -1 is the step (-1 being backwards from the last element)


'''
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
'''
def digitize(n):
    num_list = []
    for num in str(n):
        num_list.append(int(num))
    return num_list[::-1]

# one line solution -> return [int(x) for x in str(n)[::-1]]


'''
Complete the function so that it finds the average of the three scores passed to it 
and returns the letter value associated with that grade.
'''

def get_grade(s1, s2, s3):
    grade = None
    average = (s1 + s2 + s3) / 3
    grades = list('ABCDF')
    
    a = average >= 90 and average <= 100
    b = average >= 80 and average < 90
    c = average >= 70 and average < 80
    d = average >= 60 and average < 70
    f = average < 60
    
    if (a):
        grade = grades[0]
        
    elif (b):
        grade = grades[1]
        
    elif (c):
        grade = grades[2]
        
    elif (d):
        grade = grades[3]
        
    elif (f):
        grade = grades[4]
    
    return grade
    


'''
Write a program that takes any number of integers as 
input, and outputs the average and max. 
'''

str_list = list(input().split())
num_list = []

for string in str_list:
    num_list.append(int(string))

average = sum(num_list) // len(num_list)

max_num = max(num_list)

print(average, max_num)

'''
Write a program that gets a list of integers from input, and outputs 
non-negative integers in ascending order (lowest to highest). 
'''

num_list = list(input().split())

positive_nums = []

for num in num_list:
    if int(num) < 0:
        continue
    else:
        positive_nums.append(int(num))
     
        
for num in sorted(positive_nums):
    print(num, end=' ')


'''
Write a program that first takes in word pairs that consist 
of a name and a phone number (both strings), separated by a comma. 
That list is followed by a name, and your program should output the 
phone number associated with that name. Assume the search name is always in the list.

Ex: If the input is:
Joe,123-5432 Linda,983-4123 Frank,867-5309
Frank

the output is:
867-5309
'''

contacts = input().split()
contact = input()



contact_list = {}

for info in contacts:
    temp = info.split(',')
    contact_list[temp[0]] = temp[1]
    
print(contact_list[contact])


'''
Write a program to calculate the total price for car wash services. 
A base car wash is $10. A dictionary with each additional service and 
the corresponding cost has been provided. Two additional services can be 
selected. A '-' signifies an additional service was not selected. Output 
all selected services along with the corresponding costs and then the 
total price for all car wash services.
'''

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

choices = [service_choice1, service_choice2]

print('ZyCar Wash')
print('Base car wash -- $10')
for choice in choices:
    if choice in services:
        total += services[choice]
        print(f'{choice} -- ${services[choice]}')

print('----')
print(f'Total price: ${total + 10}')


'''
Implement the build_dictionary() function to build 
a word frequency dictionary from a list of words.
'''

# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer 
    # indicating that word's frequency.
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    return frequencies

# The following code asks for input, splits the input into a word list, 
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))



'''
Write a program using the given dictionary of letters and 
point values that takes a word as input and outputs the base 
total value of the word (before being put onto a board).
'''

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }    

word = input().upper()

total = 0

for letter in word:
    if letter in tile_dict:
        total += tile_dict[letter]
        
print(total)


'''
Given a sorted list of integers, output the middle integer. Assume 
the number of integers is always odd.The maximum number of inputs for 
any test case should not exceed 9. If exceeded, output "Too many inputs".
'''

num_list = list(input().split())

valid_entry = len(num_list) < 10

num = len(num_list) // 2

if valid_entry:
    print(num_list[num])
else:
    print('Too many inputs')


'''
Create a function with two arguments that will return 
a list of the first (n) multiples of (x).
Assume both the given number and the number of times 
to count will be positive numbers greater than 0. 
'''

def count_by(x, n):
    num_list = []
    count = x
    
    for i in range(n):
        num_list.append(count)
        count += x
    
    return num_list


'''
Given a string, you have to return a string 
in which each character (case-sensitive) is repeated once.
'''

def double_char(s):
    new_string = []
    for char in s:
        new_string.append(char)
        new_string.append(char)
    return ''.join(new_string)


'''
All of the animals are having a feast! Each animal is bringing one 
dish. There is just one rule: the dish must start and end with the 
same letters as the animal's name. For example, the great blue heron 
is bringing garlic naan and the chickadee is bringing chocolate cake.
Write a function feast that takes the animal's name and dish as arguments 
and returns true or false to indicate whether the beast is allowed to 
bring the dish to the feast.
'''

def feast(beast, dish):
    result = None
    
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        result = True
    else:
        result = False
        
    return result


'''
Our football team finished the championship. The result of each match look like "x:y".
 Results of all matches are recorded in the collection. For example: ["3:1", "2:2", "0:1", ...]
Write a function that takes such collection and counts the points of our team in the championship. 
Rules for counting points for each match:

    if x > y: 3 points
    if x < y: 0 point
    if x = y: 1 point

'''

def points(games):
    count = 0
    scores = []
    
    for game in games:
        scores.append(game.split(':'))
    
    
    for score in scores:
        if (score[0] > score[1]):
            count += 3
        
        elif (score[0] == score[1]):
            count += 1
            
        else:
            continue
        
    return count


'''
You ask a small girl,"How old are you?" She always says, 
"x years old", where x is a random number between 0 and 9.
Write a program that returns the girl's age (0-9) as an integer.
Assume the test input string is always a valid string. For example, 
the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

'''

def get_age(age):
    return int(age[0])



'''
The first century spans from the year 1 up to and including the year 
100, the second century - from the year 101 up to and including the year 200, etc.
Given a year, return the century it is in.
'''

def century(year):
    
    result = 0
    
    while year > 0:
        
        year -= 100
    
        result += 1

            
    return result



'''
given a string of space separated numbers, return the highest and lowest number.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers):
    
    num_list = sorted(list(map(int, numbers.split())), reverse=True)
    
    return f'{num_list[0]} {num_list[-1]}'



'''
Given a non-negative integer, 3 for example, return a string 
with a murmur: "1 sheep...2 sheep...3 sheep..."
'''

def count_sheep(n):
    count = 1
    sheep = ""
    for i in range(n):
        sheep += f"{count} sheep..."
        count += 1
    return sheep



'''
Your task is to create the functionisDivideBy (or is_divide_by) 
to check if an integer number is divisible by both integers a and b.
'''

def is_divide_by(number, a, b):
    return (number % a == 0) and (number % b == 0)



'''
Given an array of integers, remove the smallest value. Do not mutate 
the original array/list. If there are multiple elements with the same 
value, remove the one with a lower index. If you get an empty array/list, 
return an empty array/list. Don't change the order of the elements that are left.
'''

def remove_smallest(numbers):
    result = None
    
    if numbers:
        processed_numbers = numbers[:]
        processed_numbers.pop(processed_numbers.index(min(processed_numbers)))
        result = processed_numbers
    else:
        result = numbers
    
    return result



'''
Write a 'welcome' function that takes a parameter 'language' (always a string), 
and returns a greeting - if you have it in your database. It should default to 
English if the language is not in the database, or in the event of an invalid input.
'''

def greet(language):
    
    welcome_message = {
'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'
}
    message = welcome_message['english']
    
    if language in welcome_message:
        message = welcome_message[language]
        
    return message



'''
Write a program that reads a character, then reads in a list of 
words. The output of the program is every word in the list that 
contains the character at least once. Assume at least one word in 
the list will contain the given character.
'''

character = input()
word_list = input().split()

for word in word_list:
    if character in word:
        print(word)

'''
This program will store roster and rating information for a soccer team. 
Coaches rate players during tryouts to ensure a balanced team.
'''

def print_menu():
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    
    
    
def print_roster():
    print('ROSTER')
    for key in sorted(roster.keys()):
        print(f'Jersey number: {key}, Rating: {roster[key]}')
    print()

def add_player():
    player = int(input(f"Enter a new player's jersey number:\n"))
    rating = input(f"Enter the player's rating:\n")
    roster[player] = rating

def delete_player():
    player = int(input(f"Enter a jersey number:\n"))
    roster.pop(player)

def update_player():
    player = int(input(f"Enter a jersey number:\n"))
    rating = input(f"Enter a new rating player:\n")
    roster[player] = rating

def above_rating():
    rating = input(f"Enter a rating :\n")
    print(f'ABOVE {rating}')
    for key in sorted(roster.keys()):
        if roster[key] > rating:
            print(f'Jersey number: {key}, Rating: {roster[key]}')
    print()
count = 1
roster = {}

while count < 6:
    player = int(input(f"Enter player {count}'s jersey number:\n"))
    rating = input(f"Enter player {count}'s rating:\n\n")
    roster[player] = rating
    count += 1
    
print_roster()

print_menu()


option = input('Choose an option:\n')

while option != 'q':
    if option == 'a':
        add_player()
    
    elif option == 'd':
        delete_player()
    
    elif option == 'u':
        update_player()
    
    elif option == 'r':
        above_rating()
    
    elif option == 'o':
        print_roster()
    
    print_menu()
    
    option = input('Choose an option:\n')



'''
capitalize each word in a string
'''

def to_jaden_case(string):
    tokens = string.split()
    
    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace(tokens[i][0], tokens[i][0].upper(),1)
        
    return ' '.join(tokens)