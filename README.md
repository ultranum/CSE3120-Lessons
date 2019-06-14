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

3. __Polymorphism__ is the ability to instantiate objects with different values for class attributes.
    * For Example, a Honda Civic is made from the Civic class, but can have different exterior color attributes and interior finish materials attributes.
    * The advantage of polymorphism is that the program can construct many similar objects in less lines of code.
    
4. __Encapsulation__ is the process of protecting or hiding data and code so that other parts of the program can only interact with the data in pre-programmed pathways. Often times, these interactions are aggregated into an interface. The interface is a collection of setter and getter methods. (Sometimes called modifier and accessor methods.) These methods are the primary pathway to modify or retrieve object attributes.
    * For Example. a protective case encapsulates the components of a computer and the only interaction is through input and output ports.
    * It is important to only create setter and getter methods for attributes that are needed outside of the object.
    

'''
class myClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
    
    // Setter Methods
    def setX(self, x):
        self.x = x
        self.pos = (self.x, self.y)
        
    def setY(self, y):
        self.y = y
        self.pos = (self.x, self.y)
    
    // Getter Methods
    def getPos(self):
        return self.pos
'''
5. __Inheritance__ is when one class references and builds upon another class. The class inherits all attributes and methods of the referenced class, which is called the parent class. The class that does the referencing is called the child class or subclass

'''
python

class parent:
    def __init__(self, name):
        self.name = name
        
   def aMethod(self):
        pass
        
class child(parent, object):
    def __init__(self, name, age):
        parent.__init__(self,name)
        self.age = age    
'''
Inheritance reduces the amount of copied attributes and methods between classes. Python allows multiple inheritance, but many languages only allow one class inheritance.

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