#  File:       test.py
# Adding more comments
# Another comment
# Yet another
# ... and another
# ...... and another
# this was edited in master
# now we have second run in master
# it is important to be more careful with details
# and keep it as simple as possible

import random

# define the bubble sort function
def sort(values):
   length = len(values)
   for time in range(0, length-1):
      for position in range(0, (length-time-1)):
         if values[position] > values[position+1]:
            temp = values[position]
            values[position] = values[position+1]
            values[position+1] = temp

# generate a list of ten random numbers
numbers = []
number = 0
while number < 10:
   value = random.randint(1,100)
   if not(value in numbers):
      numbers.append(value)
      number = number + 1

# show unsorted list, sort the list, and show sorted list
print ("Before:", numbers)
sort(numbers)
print ("After :", numbers)
