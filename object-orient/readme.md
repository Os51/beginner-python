# Python Object Oriented Programming

## Methods
- Behaviours associated with object parameters that modify the state of an object.
- Can be referred to as functions that belong to a specific instance of a class
  - This means that calling a method on a list will only modify the instance of the list and not all lists globally.
 
- Methods fall into several categories:
  - Instance Methods
  - Class Methods
  - Static Methods

### Instance Methods
- Most common type of method in Python
- Defined within a class by creating functions inside the class definition
- Instantiating an instance of a class allows for those individual instances to have their methods called so the program can control and modify those instances directly.
- Can take a parameter called `self` which represents the instance that the method is being executed on.
  - It allows you to access attributes of the instance using dot notation, like `self.name`, which accesses the name attribute of that specific instance of the class object
- When you have variables that contain different values for different instances, these are called **instance variables**.

 ### Class Methods
 - Called for the class itself instead of the instance
 - Marked with a `@classmethod` decorator and takes a `cls` parameter that points to the class when the method is called.
 - Common use case is to create and modify dasta structutres that contain records for all instances of a class
   - Usually, programmers make a list inside the class definition, and methods to add instances of the class to that list in order to keep track of the class.

  ### Static Methods
  
