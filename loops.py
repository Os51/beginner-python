ingredients = ["Milk", "Eggs", "Flour", "Sugar"]

# For loops allow for an action to be performed on each element of the specified collection
# General structure:
# for <temp variable> in <collection>:
#  <action>
'''
Keywords
for - indicates the start of a for loop
<temporary variable> - used to represent the value of the element in the collection the loop is on
in  - separates the temporary variable from the colletion used for iteration
<collection> - what to loop over
<action> - what to do on each iteration of the loop
'''

for ingredient in ingredients:
  print(ingredient)

"""
In this example:
  - ingredient is the temp variable
  - ingredients is the collection
  - print(ingredient) is the action performed
"""

# The temp variable's name is arbitrary and doesn't need to be defined beforehand. The below will do the exact same thing.
# Examples:
for i in ingredients:
  print(i)

for item in ingredients:
  print(item)

# There is a thing in Python called an elegant loop, which allows for the loop to be written as one line and not need indentation:
for ingredient in ingredients: print(ingredient)

# This is useful for simple programs, but not recommended for any loop that has to perform multiple complex actions on each iteration.
