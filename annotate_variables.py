# Annotate Variables
# Annotation of a variable is possible but does come with computational overhead
# It is recommended not to overuse it, as it will unnecessarily add overhead to the runtime of your programs

# Standard annotation
# Think of annotation as putting a label on a container - anything in the container should hold what the label is describing

name: str = "Betty"

# The variable name is declared using a colon (:) instead of an equals sign (=). We then annotate the variable with the type 'str', indicating that the name variable should hold a string.

age: int = 34

# Here, we declare the variable "age" and annotate the type of 'int', indicating that the variable should hold an integer value.

# If a function expects a list of integers, it can be annotated with List[int], not just List:
age_list: list[int] = [23,47,81]

# We can also use comments to annotate:
captain = "Picard"  # type: str

# Duck typing is a method of inferring what a variable is by what it looks like. Adopts the ideology of: "If it walks like a duck, and quacks like a duck, it must be a duck".
a = "Hello World"  # looks like a string, so it must be a string

# Python doesn't actually require you to declare variable types unlike C# or Java. In Python, the variable can change over time as new values are assigned to it
# This is known as Dynamic Typing. Python decides which of the built-in types the variable is, and through that how it should behave.

a = 3  # a is an int
a = "Hello World"  # a is now a string.
