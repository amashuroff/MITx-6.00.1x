"""
An extended example of creating classes, hierarchy and using inheritance

Substitution principle:
    Important behaviors of the superclass should be supported by all subclasses

Generator:
    any procedure or method that have yield statement called a generator
    generators have a next() method which starts/resumes execution of the procedure.

    Inside of a generator:
        yield suspends execution and returns a value
        raise StopIteration exception when run out of yield()

    can use generator inside a looping structure, as it will continue until it gets an exception

Why generators?

generator separates the concept of computing a vary long sequence of objects,
    from the actual process of computing them explicitly

allows one to generate each new objects as needed as part of another computation,
    (rather than computing a very long sequence, only to throw most of it away,
    while you do something on an element, then repeating the process)

have already seen this idea in range()

"""
from time import time
import datetime

# creating the parent class
class Person(object):
    def __init__(self, name):
        """ create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(" ")[-1]

    def set_Birthday(self, month, day, year):
        """ sets self's birthday to birthdate"""
        self.birthday = datetime.date(year, month, day)

    def get_lastName(self):
        """ return self's last name"""
        return self.lastName

    def get_Age(self):
        """ returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        else:
            return (datetime.date.today() - self.birthday).days  # converting to days

    def __lt__(self, other):            # less than method
        """ return True if self's name is lexicographically less than other's name, False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """ return self's name"""
        return self.name


# creating a child class
class MITPerson(Person):
    nextIdNum = 0  # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)  # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)


m1 = MITPerson("Mark August")
m2 = MITPerson("Alex Mountain")
m3 = MITPerson("Student Greenwood")

# print(m1 > m2)

p1 = Person("John")
p2 = MITPerson('Steve')



# Attribute error, p2 uses __lt__ method from MIT_Person class, p1 has no id_num
# p2 < p1 will be converted into p2.__lt__(p1) which applies the method associated with the type of p2 (MIT_Person)
# print(p2 < p1)

# p1 > p2 converts to p2 < p1, thus using id_num to compare 2 instances (no __gt__ method)

# Comparing lexicographically
# print(p1 < p2)


# create a class that captures common behaviors of subclasses, concentrate methods in one place,
# think about subclasses as a coherent whole
# Student captures all the classes inside, and there is no need to change hierarchy or the methods associated with them,
# when adding new classes, or common functions



class Student(MITPerson):      # create a superclass that covers all students
    pass

class Under_Grad(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def get_class(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, "Dude " + utterance)

class Grad(Student):
    pass

class Transfer_Student(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)     # test for superclass checks for instances of subclasses

s1 = Under_Grad('Mat Buck', 2017)
s2 = Under_Grad('Foo Bar', 2019)
s3 = Grad('Billy Bird')


# creating a professor class that inherits from MIT_Person class
class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = "In course " + self.department + " we say "
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak("it is obvious that " + topic)



# Building a class that includes instances of other classes within it (Grade book)

# Concept:
   # build a data structure that can hold grades for students
   # gather together data and procedures for dealing with them in a single structure,
       # so that users can manipulate without having to know internal details.



class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []      # list of Student objects
        self.grades = {}        # maps idNum -> list of grades
        self.isSorted = True    # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:    # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')


    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        # return self.students[:] (copy of list of students)
        # instead of returning copy of an entire list, use generator (one at a time)
        for s in self.students:
            yield s



def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


st1 = Under_Grad("Alex Moon", 2002)
st2 = Under_Grad('Moon Bay', 2003)

six00 = Grades()
six00.addStudent(st1)
six00.addStudent(st2)
six00.addGrade(st1, 90)



# print(six00.allStudents())
# print(gradeReport(six00))

# can list all students using:
for s in six00.allStudents():
    print(s)
# prints out all student names using sorted by idNum

for s in six00.students:
    print(s)
# this for loop violates the data hiding aspect of an object,
# exposing internal representation
# if i were to change how i represent the grade book,
# i should only need to change the methods within that object, not external procedures, that use it.

# current version of the grade book is inefficient
# to get list of all students, i create a copy of an internal list
# imagine 100.000 students in a MOOC



# generator example, fib numbers
def genFib():
    fibn_1 = 1      # fib(n-1)
    fibn_2 = 0      # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

# print(genFib().__next__())


# generator example, prime numbers
def genPrimes():
    primes_lst = []
    last_prime_num = 1

    while True:
        last_prime_num += 1
        for p in primes_lst:
            if last_prime_num % p == 0:
                break
        else:
            primes_lst.append(last_prime_num)
            yield last_prime_num

# generators vs list comprehension
gen_start = time()
# print(sum(n for n in range(100000000)))
gen_end = time()
gen_time = gen_end - gen_start

list_start = time()
# print(sum([n for n in range(100000000)]))
list_end = time()
list_time = list_end - list_start

# generator is faster
# print(f'sum(n for n in range(10000000)) took {gen_time} secs')
# print(f'sum([n for n in range(10000000)]) took {list_time} secs')

