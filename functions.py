# num = int(input("Enter number: "))

def is_even(i):# the i is parameter
    """checking if the number entered is
     even or odd"""
    if type(i) ==int:
        if i%2==0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'enter an integer value'


for i in range(1,11):
    x = is_even(i)
    print(x)

print(is_even('hello')) # the hello is argument

# types of argument:

## default argument

#
def power(a=1,b=1):
    return a**b

print(power())

## positional arguments
## key word argument

# args amd kwargs
# allows us to pass a variable number of non-keyboard arguments to a function

# in this program we have to explicitly define how many parameters are possible
def multiply(a=1,b=1,c=1):
    return a*b*c

multiply(1,2)

# by using we can  remove the limited parameters
def multiply(*args):
    prod =1
    for i in args:
        prod=prod*i
    return prod
print(multiply(1,23,9,4,5,9,6,7,8))

print(print.__doc__) # .__docs__ used to summon documentation of the python

# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,'->',value)

display(india='Delhi',china='shanghai',america='washington dc')