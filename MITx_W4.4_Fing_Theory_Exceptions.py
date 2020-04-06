'''
Other types of exceptions:
    SyntaxError - Python can't parse(разбирать) program

    NameError - local or global name not found

    AttributeError - attribute reference fails

    TypeError - operand doesn't have correct type, operation is applied to a value of an inappropriate type

    ValueError - operand type is okay, but value is illegal

    IOError - IO system reports malfunction (file not found)

What to do, when encounter an error?
    - fail silently:
        substitute values, or carry on (bad idea)
    - return an 'error' value:
        what value to choose?
        complicates code having to check for a special value
    - stop execution, signal error condition:
        in Python, raise an exception:

Parser - синтаксический анализатор

try: do something

except: do if there was an exception caught while trying
        (there can be more than one)
else: do if there is no exception but before finally

finally: do this, ALWAYS, at the end

then any further lines are normal program flow
so do something after finally if no uncaught exception crashed the program
'''

# dealing with exceptions
# exception raised within the body of the try are handled by except statement and execution continues after the
# body of the except statement
try:
    a = int(input('Enter a num: '))
    b = int(input('Enter another num: '))
    print(a/b)
    print('Okay')
except ValueError:
    print('Could not convert to a number')
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print('Something went very wrong!!!')

# else: body of this is executed if try body completes with no exceptions
# finally: body of this is always executed after try, else and except statements,
# even if they raised another error, executed a break, continue or return
# finally is useful for clean-up code that should be run no matter what else happened (e.g. close a file)


# can store exceptions as variables
# except IndexError as e:
    # print(e)

# exceptions usage example
while True:
    try:
        n = input("Please enter the num: ")
        n = int(n)
        break
    except ValueError:
        print('Input not an integer, try again')
        # also can perform different operations


# Exceptions as control flow
# raise an exception when unable to produce a result consistent with the function specifications
# raise ValueError("Something is wrong")

def get_ratios(L1,L2):
    """

    :param L1: list of nums
    :param L2: list of nums
    assumes L1 and L2 are of equal length
    :return: List containing L1[i]/L2[i]
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))    # not a number
        except:
            raise ValueError("get_ratios called with bad arguments")
    return ratios

L1 = [1,2,3]
L2 = [2,3,0]

# print(get_ratios(L1, L2))



# control flow example
def get_stats(class_list):
    '''
    :param class_list: list of lists with names and grades
    :return: list with the list of names, grades and average of grades
    '''
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:       # here is an example of using except as control flow
        print('no grades data')
        return 0.0


# f.ex 1
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]  # 2
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

# print(fancy_divide([0,2,4], 0))
# when running this piece of code, we get 0, then ZeroDivisionError
# Python executes finally statement first, and only after it raises an error

# f.ex 2
def fancy_divide1(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

# print(fancy_divide1([0,2,4], 0))
