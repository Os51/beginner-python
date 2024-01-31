# defining a function starts with "def" keyword
# after this is the name of the function. the name can be anything but should be something that makes sense to what the function's purpose is.
# after this is the parameter of the function, written in parenthesis (). This can be optional if not defined, and mandatory if defined. 
# when the function is called, if defined, the parameter must be included else it will result in an error.
# the indentation after the definition is the body of the function - as in what the function is to do when it's called.

def greeting(name):
  print("Welcome, " + name)

def full_greeting(name, department):
  print("Welcome, " + name)
  print("You are a member of " + department)

greeting("Ellie")
full_greeting("Ellie", "IT Support")

# Built-In Functions
# - Functions that exist in Python and can be called directly
"""
List of built-in functions:
print() - outputs a specified object to the screen
type() - returns the data type of its argument. It may be passed to another function, like print, for output.
str() - convert any data type to a string
sorted() - sorts the components of a list. 
  Also works on any iterable (like a string) and returns the sorted elements in a list. 
  Default sort is ascending order. Note that it does not change the iterable that it sorts.
min() - returns the smallest numeric input passed to it
max() - returns the largest numeric input passed to it
"""
