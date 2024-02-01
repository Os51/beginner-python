# Conditionals

## Comparing things
Python can be used to compare values. We can check if something is smaller than, equal to, or bigger than something else. We can take the result of a comparision expression and use it to make a decision. 
With comparisions, the result can either be **true** or **false**. This data type is known as a Boolean value. 
### Logical Operators
- `and` - To evaluate as "True", the `and` operand would need both expressions to be true.
  - If just one expression is false, the operand result is False 

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
