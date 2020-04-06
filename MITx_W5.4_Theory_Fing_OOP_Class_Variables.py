"""
Instance variables vs Class variables:

Instance vars:
    - specific to an instance
    - created for an instance, belongs to an instance
    - uses the generic name variable 'self' within the class definition (self.variable_name)

Class vars:
    - belong to the class
    - defined inside the class, but outside any class methods, outside __init__
    - shared among all objects/instances of that class

"""


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None  # is a data attribute, even if not initialized

    def get_age(self):
        return self.age  # getters, access data attributes

    def gen_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age  # setters, changing bindings for attributes

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return "animal: " + str(self.name) + " : " + str(self.age)


class Rabbit(Animal):
    tag = 1  # class variable

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rabbit_id = Rabbit.tag  # accessing class variable
        Rabbit.tag += 1  # incrementing class variable changes it for all instances that may reference it

    def speak(self):
        print('meep!')

    def __str__(self):
        return 'rabbit: ' + str(self.name) + ' : ' + str(self.age)

    def get_rabbit_id(self):
        return str(self.rabbit_id).zfill(3)  # method on a string to pad the beginning with zero's

    def parent1(self):
        return self.parent1

    def parent2(self):
        return self.parent2

    def __add__(self, other):
        # returning object of the same type as this class
        return Rabbit(0, self, other)  # mating the rabbits

    def __eq__(self, other):
        # decide if 2 rabbits are equal if they have the same 2 parents
        # comparing id's of the rabbits, since id's are unique (due to class vars)

        parents_same = self.parent1.rabbit_id == other.parent1.rabbit_id \
                       and self.parent2.rabbit_id == other.parent2.rabbit_id

        parents_opposite = self.parent1.rabbit_id == other.parent2.rabbit_id \
                           and self.parent2.rabbit_id == other.parent1.rabbit_id

        return parents_opposite or parents_same

