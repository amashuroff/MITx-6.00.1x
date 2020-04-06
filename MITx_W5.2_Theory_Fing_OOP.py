"""

Power of OOP:
    Bundle together objects that share:
        - common attributes
        - procedures that operate on those attributes
    Use abstraction to make a distinction between how to implement an object vs
        how to use the object.
    Build layers of object abstractions that inherit behaviours from other classes of objects
    Create our own classes of objects on top of Python basic classes

Implementing the class VS Using the class:

Implementing a new object type with a class:
    - define a class
    - define data attributes (what IS the object)
    - define methods (HOW to use the object)

Using the new object type in code:
    - create instances of the object type
    - do operations with them

Groups of obejcts has attributes:
    Data attributes:
        How you can represent your object with data?
        what IT IS?
        age, name, coordinate x,y

Procedural attributes:
    Behavior, operations, methods
    What kinds of things you can do with the object?
    what IT DOES?
    distance between 2 coordinates, make sounds, draw a picture

Information hiding:
    Getters and Setters:
        - should be used outside of the class to access data attributes
        - use getters to separate internal representation from access of that representation

    a.age - directly accessing data attribute
    a.get_age() - access and use method:
        easy to maintain
        good style
        prevents bugs

    if you accessing data attributes outside of the class and class definition changes, may get errors

    Python NOT great at information hiding:

    - allows to access data from outside class definition (print(a.age)
    - allows you to write data from outside class definition (a.age = 'infinite')
    - allows you to create data attributes for an instance from outside class definition (a.size = 'big')

    - it is NOT a good style to do any of these (always write a method to store new attributes inside of it to access
        using getters the attribute values that you want out there)

Self determined from instance, passed as an argument:
    - for the method def __init__(self, age):
        * creates self, passes it in automatically as argument
        * a = Animal(3)
    - for the method def get_age(self):
        * call method using a.get_age()
        * or alternatively Animal.get_age(a)

Default arguments for formal parameters are used if no actual argument is given:
    - for the method def set_name(self, name = ""):
        * default argument used here a.set_name()
        * argument passed is used here a.set_name("Fluffy")

"""

# example
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None    # is a data attribute, even if not initialized

    def get_age(self):
        return self.age             # getters, access data attributes
    def gen_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age          # setters, changing bindings for attributes
    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return "animal: " + str(self.name) + " : " + str(self.age)

