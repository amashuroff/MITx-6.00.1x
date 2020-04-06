'''
Classes are like blueprints, we use them to represent an abstract notion or idea of how we describe real world objects
 according to certain criteria.


Every object has:
    Type
    Internal data representation (primitive or composite)
    a set of procedures for interaction with an object

Each instance is a particular type of object

Everything in Python is an object and has a type

Objects are data abstractions that capture:
 - internal representation through data attributes
 - interface for interacting with objects through methods (procedures):
     defines behavior but hides implementation

Can create new instances of objects

Can destroy objects:
    del
    or just 'forgetting' about them (Python sys. will reclaim destroyed or inaccessible objects - called "garbage collection"

Example:
    [1,2,3] - is of type list, meaning it is an instance of the list

Make a distinction between creating the class and using an instance of that class:
    - creating class involves:
        defining the class name
        defining class attributes
    - using class involves:
        creating new instances of objects
        doing operations on the instances

Advantages of the OOP:
    - bundle data into packages together with procedures that work on them through well-defined interfaces
    - treating as an abstraction (abstract data representation)
    - divide-and-conquer development:
        implement and test the behavior of each class separately
        increased modularity reduces complexity
    - classes make it easy to re-use code:
        many Python modules define new classes
        each class has a separate environment (no collision on function names)
        inheritance allows subclasses to redefine or extend a selected subset of a superclass's behavior


Instances, attributes, methods

Attributes:
    think of them as objects that make up the class
    for example: coordinate is made up of 2 numbers
Methods:
    think of methods as functions that only work with this class

Creating attributes and methods for the class:
    attributes:
        self.attributeName = variableName
    methods:
        def breath(self)
       calling methods: instanceName.methodName()

Instances are specific and concrete examples that belong to a class.
Instances have their own individual values for each one of these attribute categories defined in the class.
OOP provides the blueprint to create individual instances that share the same structure but have their own set of characteristics

'''

# F.ex 1
# What does the code print out?
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

# clock = Clock('5:30')
# clock.print_time()
# answer is 5:30, since we print out the attribute, not the local variable

# F.ex 2
# What does the code print out?

class Clock(object):
    def __init__(self, time):
        self.time = time
        def print_time(self, time):
            print(time)


# clock = Clock('5:30')
# clock.print_time('10:30')
# answer is 10:30. Giving parameters with the same name as object attributes may be confusing
# give parameters, local variables, and attributes different, distinct names to avoid the confusion that arises in this problem.

# F.ex 3
# What does the code print out?


class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()
# answer is 10:30. paris_clock and boston_clock are 2 names for the same object. Aliasing

# Class examples

# Fraction
class Fraction(object):
    def __init__(self,numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer)  + ' / ' + str(self.denom) # string representation using print

    def getNumer(self):     # defining getters (allow to access data attributes)
        return self.numer   # getter will allow to separate out accessing the internal representation
                            # from the actual use of the representation
    def getDenom(self):
        return self.denom

    def __add__(self, other):   # takes in instance itself and some other fraction (instance)
        numerNew = other.getDenom() * self.getNumer() \
                   + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)   # creating a new instance

    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)

    def convert(self):
        return self.getNumer() / self.getDenom()

# one = Fraction(1,2)
# two = Fraction(1,2)
# three = one - two
# print(three)

# Set of integers

# create a new type to represent collection of integers
# initially the set is empty
# particular integer appears only once in a set:
    # representational invariant enforced by the code
# internal data representation:
    # use a list to store the elements of the set
# interface:
    # insert(e) - insert integer e into set if not there
    # member(e) - return True if integer e in the set
    # remove(e) - remove integer e from the set, error if not present

class intSet1(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the self.vals appears exactly once
    """
    def __init__(self):
        """
        Create an empty set of integers
        """
        self.vals = []

    def insert(self,e):
        """
        :param e: is an integer
        :return: inserts e into self
        """
        if not e in self.vals:
            self.vals.append(e)

    def member(self,e):
        """
        :param e: int
        :return: True if e in self
        """
        return e in self.vals

    def remove(self,e):
        """
        :param e: int
        :return: removes e from self, raises ValueError otherwise
        """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + "not found")

    def __str__(self):
        """
        :return: string representation of self
        """
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ','
        return '{' + result[:-1] + '}'

# Coordinate
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        # First make sure `other` is of the same type
        assert type(other) == type(self)
        # Since `other` is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

# one = Coordinate(1, 2)
# two = Coordinate(2,3)
# three = one == two


# Intersect

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self,other):
        common_set = intSet()
        for values in self.vals:
            if other.member(values):
                common_set.insert(values)
        return  common_set

    def __len__(self):
        return len(self.vals)



