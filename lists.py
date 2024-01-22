"""
List Methods

.count() - List method to count the number of occurrences of an element in a list
.insert() - List method to insert and element into a specific index of a list
.pop() - List method to remove an element from a speicifc index or from the end of a list
range() - Python function to create a sequence of integers
len() - Python function to get the length of a list
.sort() / sorted() - A method and built-in function to sort a list
"""

# Insert expects 2 inputs - first being a numerical index and the second input is any value
# All elements from the specified index and up to the last index are shifted one index to the right
# example: variable_list.insert(2, "Hi")

# Using .insert() methond
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0,"Pineapple")
print(front_display_list)

# Remove by Index using .pop()
# .pop() returns the value that was removed, so you can print it if you needed to by assigning a variable to the call

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)


# Consecutive Lists - Range
# Leverage range and list to create a list of consecutive numbers
number_list = range(9)
print(list(number_list))

# Range can have a start and end point.
number_list = list(range(0, 9)) # First number is inclusive, last number is exclusive
# This will output [0, 1, 2, 3, 4, 5, 6, 7, 8]


# Range can also "skip" numbers with a third input
number_list = list(range(5, 15, 2))
# This would output: [5, 7, 9, 11, 13]
