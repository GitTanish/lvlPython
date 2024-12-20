# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,
# but can only have one expression.
from os import lseek

# x -> x^2
a=lambda x:x**2
print(a(2))

#  x -> x+y
a = lambda x,y:x+y
print(a(2,3))

#### Diff between lambda vs Normal Function

# - No name
# - lambda has no return value(infact,returns a function)
# - lambda is written in 1 line
# - not reusable
#
# Then why use lambda functions?<br>
# **They are used with Higher Order Function**

# check if a string has 'a'
a=lambda s:'a' in s
print(a('hello'))

# odd or even
a = lambda x:'even' if x%2 ==0 else 'odd'
print(a(6))

## Higher order function :- function which returns function
def square(x):
    return x**2

def transform(f,L):
    output = []
    for i in L:
        output.append(f(i))

    print(output)

L = [1,2,3,4,5]
transform(lambda x:x**3,L)

# square the items of a list
print(list(map(lambda x:x**2,[1,2,3,4,5])))

# odd/even labelling of list items
L = [1,2,3,4]
print(list(map(lambda x:'even' if x%2==0 else 'odd',L)))

# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

print(list(map(lambda users:users['gender'],users)))

# filter
# numbers greater than 5
L = [3,4,5,6,7]

list(filter(lambda x:x>5,L))

# fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']

list(filter(lambda x:x.startswith('a'),fruits))

# reduce
# sum of all item
import functools
 
functools.reduce()