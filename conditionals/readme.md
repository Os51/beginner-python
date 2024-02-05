# Conditionals

Python can be used to compare values. We can check if something is smaller than, equal to, or bigger than something else. We can take the result of a comparision expression and use it to make a decision. 
With comparisions, the result can either be **true** or **false**. This data type is known as a Boolean value. 

!!! Boolean
- Represents one of two states: **True** or **False**
- When comparing things in Python, the result is a Boolean of the appropriate value.

___
## Comparison Operators
- These operations determine the result when comparing one value to another.
- Comparison can be to see whether a value is greater than `>` and less than `<`

```python
print(1 != 2)  # True
```
- Comparisons can be done with numbers as well as strings. If we use greater than and less than on strings, it normally refers to alphabetical order.

```python
print("Yellow" > "Cyan" and "Brown" > "Magenta")
```
- In this example, Yellow comes after Cyan, but brown doesn't come after Magenta. The whole result is therefore false as we're using the `and` operator.


- We can't normally compare two different data types to each other using these operators as it will result in an error
```python
print(1 > "1")  # Results in an error
```

___
## Equality Operators
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
