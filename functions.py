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
