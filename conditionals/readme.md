# Conditionals

Python can be used to compare values. We can check if something is smaller than, equal to, or bigger than something else. We can take the result of a comparision expression and use it to make a decision. 
With comparisions, the result can either be **true** or **false**. This data type is known as a Boolean value. 

> **_NOTE:_** Boolean: Represents one of two states: **True** or **False**. Boolean is its own data type and _not_ a string.


___
## Comparison Operators
- These operations determine the result when comparing one value to another.
- The operators include:
  - `>` - Greater Than
  - `<` - Less Than
  - `>=` - Greater Than or Equal To
  - `<=` - Less Than or Equal To 

```python
print(1 != 2)  # True
```

- We can't normally compare two different data types to each other using these operators as it will result in an error
```python
print(1 > "1")  # Results in an error
```

### Comparison Operators with Strings
- Comparisons can be done with numbers as well as strings. If we use greater than and less than on strings, it normally refers to alphabetical order.

```python
print("Yellow" > "Cyan" and "Brown" > "Magenta")
```
- In this example, Yellow comes after Cyan, but brown doesn't come after Magenta. The whole result is therefore false as we're using the `and` operator.

- Python comparison operators return Boolean results with strings.

| Expression | Result |
| ---------- | ------- |
| "a" == "a" | String "a" is identical to string "a". Returns True. |
| "a" != "b" | String "a" is not identical to string "b". Returns True. |
| "a" > "b" | Does string "a" have a larger Unicode value than string "b". Returns False.|
| "a" < "b" | Does string "a" have a smaller Unicode value to string "b" |

#### Unicode values for the alphabet
| Unicode Number | Character | Unicode Number |  Character |
| 65 | A | 97 | a |
| 66 | B | 98 | b |
| 67 | C | 99 | c |
| 68 | D | 100 | d |
| 69 | E | 101 | e |
| 70 | F | 102 | f |
| 71 | G | 103 | g |
| 72 | H | 104 | h |
| 73 | I | 105 | i |
| 74 | J | 106 | j |
| 75 | K | 107 | k |
| 76 | L | 108 | l |
| 77 | M | 109 | m |
| 78 | N | 110 | n |
| 79 | O | 111 | o |
| 80 | P | 112 | p |
| 81 | Q | 113 | q |
| 82 | R | 114 | r |
| 83 | S | 115 | s |
| 84 | T | 116 | t |
| 85 | U | 117 | u |
| 86 | V | 118 | v |
| 87 | W | 119 | w |
| 88 | X | 120 | x |
| 89 | Y | 121 | y |
| 90 | Z | 122 | z |



### Equality Operators
- Operation to determine if a value is equal to another value.
- Equality is determined with the `==` operation, or not equal `!=`.

```python
print("cat" == "dog")  # False
```
- The example evaulates to false as the string "cat" is not the same as "dog"

- We can also use equality comparison on a string and int value, which is a different case to if we were trying to run an equation between the two (which normally presents an error)

```python
print(1 != "1")  # True
print(1 == "1")  # False
```
- Python knows that the data types are different, so though the values are the same, it still evaluates to false as 1 as int does not equal 1 as string (string does not equal int)

___
## Logical Operators
- `and` - To evaluate as "True", the `and` operand would need both expressions to be true.
  - If just one expression is evaluated to be false, the entire operand result is **False** 

```python
print(4 < 6 and 3 < 6)  # True
print(4 < 6 and 3 > 6)  # False
```

- `or` - To evaluate as "True", the `or` operand would only need one of the expressions to be true
  - If both are false, the operand result is False. If both are true, the operand result is True

```python
print(4 < 6 or 3 > 6)  # True
```

- `not` - Inverts the value of the expression that is infront of it. If the expression is true, it become false. If it is false, it becomes true.

```python
print(not 4 < 6)  # False
```


___
# Branching
- Ability of a program to alter its execution sequence

## Branching using if statements
- The function within an if statement will only run if the condition is evaluated as True, else it is skipped.

```python
def validate_username(username):
  if len(username) < 3:
    print("Username is invalid. Must be at least three characters long")
```
- In the example, the function will only output if the variable "username" is less than three characters long.

## Branching using if/else
- You can add a condition to run if the value of the if statement is **not** true.

```python
def validate_username(username):
  if len(username) < 3:
    print("Username is invalid. Must be at least three characters long")
  else:
    print("Valid username")
```

- This will evaluate based on the string in variable "username"
  - If the length is less than three, the response from the if statement is activated
  - If the length is more than three, the response from the else statement is activated

- The else statement is useful but we don't always need to use it.
- If we want to define a function that checks whether a number is positive or not, it can be written like this:

```python
def is_positive(number):
  if number > 0:
    return True
  else:
    return False
```
- However, we don't need to explicitly define an else function if using Return:

```python
def is_positive(number):
  if number > 0:
    return True
  return False
```
- When a return statement is executed, the function exists so that the code that follows doesn't get executed. In this case, if the number is larger than zero, the first Return statement is triggered and the function exits as a result.


## Branching with if/elif/else
- If and else blocks allow branch execution depending on whether a condition is True of False
- Using elif (else-if), we can add additional conditions and outcomes to a function.
- The condition must be evaluated as True for the body of the elif block to be executed

```python
def validate_username(username):
  if len(username) < 3:
    print("Invalid username. Must be at least 3 characters long")
  elif len(username) > 15:
    print("Invalid username. Must be less than 15 characters")
  else:
    print("Valid username")
```
