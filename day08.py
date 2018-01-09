def say_hello():
    """Prints hello"""
    # insert code in here to print hello
    print('hello')



# Print hello
say_hello()

def forty():
    """Returns 40"""
    # insert code in here to return 40
    return 40


# Should print 80
print(forty() * 2)

def add_them_all(v1, v2, v3, v4):
    """Returns sum of five numbers"""
    #insert code in here to return the sum of all 4 arguments
    x = v1 + v2 + v3 + v4
    return x
# Should be 200
print(add_them_all(1, 9, 20, 170))

from math import sqrt
def find_hypotenuse(a, b):
    """Returns the hypotenuse of a triangle"""
    c = sqrt(a**2 + b**2)
    return c
print(find_hypotenuse(3, 4))