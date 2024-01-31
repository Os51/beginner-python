# Study Guide: Python Functions

## Key Terms
- **Return Value** - value or variable returned as the end_result of a function
- **Parameter (argument)** - a value that is passed into a function for use within the function
- **Refactoring** - a process to restructure code without changing functionality

## Things to remember
- Python has built in functions that can be used to perform different tasks:
  - `print()` - output to console/screen
  - `type()` - display the data type of what object passed to it. This needs to be coupled with print() to output to screen
  - `str()` - convert to string data type
  - `sorted()` - sorts any iterable value in ascending order. Does not change the values of the iterable
  - `min()` - reports the smallest value
  - `max()` - reports the largest value


## Cliff Notes
- The `def()` keyword is used to define a new function
- For best practices when writing code that is **readable** and **reusable**:
  - **Create a reusable function** - Replace duplicate code with one reusable function to make the code easier to read and repurpose.
  - **Refactor Code** - Update code so it is self-documenting and the intent of the code is clear
  - **Add comments** - Adding comments is part of self-documenting code.
    - Use comments to leave notes for yourself or other programmers to make the purpose of the code clear.


_Duplicate code_
```python
name = "Jeff"
number = len(name) * 6
print("Hello " + name + ". Your number is " + str(number))

name = "Steve
number = len(name) * 6
print("Hello " + name + ". Your number is " + str(number))
```

_Reusable function that improves readability_
```python
def greeting(name):
  number = len(name) * 6
  print("Hello " + name + ". Your number is " + str(number))

greeting("Jeff")
greeting("Steve")
```

