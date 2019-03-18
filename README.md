# CSE3120-Lessons Object Oriented Programming 1

## Definitions

__Object oriented programming (OOP)__ is the process of implementing Object-oriented Design in a functional program.

__Object Oriented Design (OOD)__ is the process of converting identifiable objects and their interactions into a template to construct any number of similar objects with similar properties and interactions.

A ___Class___ is a model of an object. Classes contain the _attributes_ and _behaviours_ which are present in all objects made from this model. A class can be thought of as a template or blueprint for making an object.
    - An example of a class is a _student_
    - An attribute is a property or characteristic that the object possesses. It is stored as a variable within the object.
        - the student class has an attribute, Student ID Number.
    - A behaviour is called a method and is something the object can do. It is represented as a function within the object.
        - the student class has a method, take notes.
        
An ___Object___ is a unique set of data and functions _instantiated_ from a class. An object accesses attributes and methods using _dot notation_, which identifies the object, then calls the method within it.

## Why OOP?
1. __Abstraction__ is the process of setting the level of detail and complexity to what is appropriate for the given task.
    - Eg. A student has many properties (i.e. hair color, height, etc), but only ones relevant to the task, such as calculating an average is needed (i.e. ID, Course, Grades, etc)

2. __Aggregation and Composition__ is the process of creating a complex object by collecting several other objects. Aggregates have no relation between the collected objects. (I.e, the cards in a player's hand.) Whereas, objects in a composite are interacting to create a more complex object. The removal of an object in a composite can compromise the functionality of the composite object. (I.e, A bicycle is composed of a frame, bike chain, pedals, wheels, etc.).
## Unified Modeling Language
A standardized modeling language that has the same notational system when describing data management and software design. This language is programming agnostic and does not require a programming background to utilize. It is composed of three diagram types: structure, behavior, and interactions.

NOTE: While software developers use all three types, we will only focus on structure.

A _Class Diagram_ contains the name of the class, the attributes, and the methods.

| Bank Account | |
| --- | --- |
| _Attributes/Methods_ | _Value_ |
| - | - |
| AccountNo | Int |
| Balance | Float |
| - | - |
| withdraw(val) | Float |
| deposit(val) | Float |
| getBalance() | Float |

## Special Variables and Magic Methods
__Special Variables__ classes and objects have properties that are already built-in attributes within the programming language.
    * A special variable in python is denoted with two underscores before and after the variables name.
    * These variables can also be called double underscore variables or dunder variables
__Magic Methods__ are methods within a class that redefines or manipulates special variables.

'''

class myClass:
    def __init__(self, name):
        self.name = name
        
    def __str__ (self):
        return "class name is " + self.name
'''