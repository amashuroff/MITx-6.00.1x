
# Problem 3
# Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels,
# according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

# For example, if s = "This is great!" then print_without_vowels will print Ths s grt!.
# If s = "a" then print_without_vowels will print the empty string .
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    vowels = 'aeiou'
    if len(s) < 2 and s in vowels:
        print(" ")
    else:
        new = "".join([c for c in s if c not in vowels])
        print(new)

# print(print_without_vowels(""))


# Problem 4
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    max = 0
    element = None
    if len(L1) != len(L2):
        return False
    else:
        for el_1 in L1:
            min = 0
            for el_2 in L2:
                if el_1 == el_2:
                    min += 1
                    if min > max:
                        max = min
                        element = el_1
        return (element, max, type(element))

# L1 = [1, 'b', 1, 'c', 'c', 1]
# L2 = ['c', 1, 'b', 1, 1, 'c']
# print(is_list_permutation(L1, L2))


# Problem 5
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    key_code = {}
    decoded = ""
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    for c in code:
        decoded += key_code[c]
    return (key_code, decoded)

# print(cipher("abcd", "dcba", "dab"))


# Problem 7
### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    locations = []
    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        Campus.__init__(self, center_loc)
        self.tent_loc = tent_loc
        MITCampus.locations.append(self.tent_loc)

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """

        for loc in MITCampus.locations:
            if abs(new_tent_loc.dist_from(loc)) < 0.5 or new_tent_loc in MITCampus.locations:
                return False
        MITCampus.locations.append(new_tent_loc)
        return True



    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if tent_loc not in MITCampus.locations:
            raise ValueError
        else:
            MITCampus.locations.remove(tent_loc)


    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        tents = []
        for loc in MITCampus.locations:
            tents.append(loc.__str__())
        return tents


# c = MITCampus(Location(-1,-2))
# print(sorted(c.get_tents()))

