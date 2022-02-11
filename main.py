"""
program that takes age, weight, heart rate, and minutes of exercise as input,
then returns number of calories burned
"""
# user inputs
age = int(input('> '))
weight = int(input('> '))
heartRate = int(input('> '))
minutes = int(input('> '))

# calculate calories burned
calories = ((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * minutes / 8.368

# output results with 2 decimal places
print(f'Calories: {calories:.2f} calories')
