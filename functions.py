# num = int(input("Enter number: "))
from time import perf_counter


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

# Variable scope
def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

def h(y):
    global x
    x += 1
x = 5
h(x)
print(x)

def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

# nested functions

def f():
    def g():
        print('inside the function g')
    g()
    print('inside function f')

f()

# def f():
#     def g():
#         print('inside the function g')
#     g()
#     print('inside function f')
# infinite loop

def g(x):
    def h():
        x='abc'
    x=x+1
    print('in g(x):x=',x)
    h()
    return x
x= 3
z=g(x)

def g(x):
    def h(x):
        x=x+1
        print("in h(x): x = ", x)
    x = x+1
    print('in g(x): x = ', x)
    h(x)
    return x

x=3
z=g(x)
print('in main program scope: x = ',x)
print('in main program scope: z = ',z)

# functions in python are first class citizens along with data types

# type and id
def square(num):
  return num**2

print(type(square))
print(id(square))

# reassign
x = square
x(9)
print(x(9))
print(id(x))

# deleting a function
del square

def square(num):
  return num**2

# storing a function
L = [1,2,3,square]

# returning a function
def f():
    def x(a=1,b=1):
        return a+b
    return x

val= f()(3,4)
print(val)

# function as argument

def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_b')
    return z()

print(func_b(func_a)) 