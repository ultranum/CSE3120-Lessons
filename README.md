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