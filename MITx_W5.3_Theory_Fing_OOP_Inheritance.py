"""
Subclass can have methods with the same name as superclass
Subclass can have methods with the same name as other subclasses
For an instance of the class, look for a method name in current class definiton
If not found, look for method name up the hierarchy (parent, grandparent, and so on)
Use first method up the hierarchy that you found with that method name

The first thing is that there are two things happening. Some attributes are defined by __init__ and some by inheritance.

__init__ VS inheritance:

    If something is defined by __init__ then when you run the init functions, if two of them define the same thing,
    then the last one overwrites the first one and you're left with the last version initialized. The last one wins.

    Inheritance works the opposite way - you go up the tree, searching left & up first but as soon as you find
    the attribute/method you stop so there is no overwriting. The first one wins.

"""
import random

# superclass
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

# child class that inherits from the Animal class
# uses __init__ from the Animal class
# instances of type Animal will throw an error if called with new method
class Cat(Animal):
    def speak(self):
        print('meow!')
    def __str__(self):
        return 'cat: ' + str(self.name) + ' : ' + str(self.age)     # overrides __str__ from Animal class

# can still get to the Animal __str__ method using
# print(Animal.__str__(instance))


class Rabbit(Animal):
    def speak(self):
        print('meep!')
    def __str__(self):
        return 'rabbit: ' + str(self.name) + ' : ' + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)      # calling the Animal constructor
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends
    def add_friend(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)
    def speak(self):
        print('Hello!')
    def age_diff(self, other):
        diff = self.age - other.age
        # alternative way: diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, ' is ', diff, " years older than ", other.name)
        else:
            print(self.name, ' is ', abs(diff), " years younger than ", other.name)
    def __str__(self):
        return "person: " + str(self.name) + " : " + str(self.age)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")

    def __str__(self):
        return 'student: ' + str(self.name) + " : " + str(self.age) + ' : ' + str(self.major)


# Finger exercise, spell
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


def studySpell(spell):
    print(spell)


# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())

# Finger exercise. __init__ vs Inheritance
# see the module's docstring
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# obj = D()
# print(obj.a)
# print(obj.b)
# print(obj.c)
# print(obj.d)
# obj.x()
# obj.y()
# obj.z()