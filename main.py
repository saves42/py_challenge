"""
program that takes age, weight, heart rate, and minutes of exercise as input,
then returns number of calories burned
"""
# user input
age = int(input('> '))
weight = int(input('> '))
heartRate = int(input('> '))
minutes = int(input('> '))

# calculate calories burned
calories = ((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * minutes / 8.368

# output results with 2 decimal places
print(f'Calories: {calories:.2f} calories')

"""
program that takes number of quarters, dimes, nickels, and pennies as input,
and outputs total amount of money
"""
# user input
quarters = int(input('> ')) * 0.25
dimes = int(input('> ')) * 0.10
nickels = int(input('> ')) * 0.05
pennies = int(input('> ')) * 0.01

# process input
total = quarters + dimes + nickels + pennies

# output results with 2 decimal places
print(f'Amount: ${total:.2f}')