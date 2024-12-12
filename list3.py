#   list functions
# len/min/max/sorted

l = [2,3,6,4,1]
print(len(l))
print(min(l)) # works only on homogenous data
print(max(l))
print(sorted(l)) # not permanent
print(sorted(l,reverse=True))

# count
l = [1,2,3,4,5,1]
print(l.count(1))
# index # finds the index
print(l.index(5))
# reverse # permanently reverses
l.reverse()
print(l)
# sort (vs sorted) # sort is permanent, sorted isn't
l = [2,6,1,5,3,4,7,8]
l.sort()
print(l)


# copy -> shallow copy
L = [2,1,5,7,0]
print(L)
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))

# List Comprehension

# Add 1 to 10 number to a list
l =[]
for i in range(1,11):
    l.append(i)
print(l)

l = [i for i in range(1,11)] #done only in one line
print(l)

# scalar multiplication on a vector
v = [2,3,4] #scalar
s = -3 # vector

x =[]
for i in v:
    i=i*s
    x.append(i) # or x.append(i*s)
print(x)

l = [i*s for i in v]
print(l)

# add squares
l = [2,3,4,5]
print([i**2 for i in l])

# print all the numbers divisible by 5 in range of 1 to 50

l = [i for i in range(1,51) if i%5 ==0]
print(l)

# find languages which start with letter p
languages = ['java','python','php','c','javascript']

print([language for language in languages if language.startswith('p')])
print([i for i in languages if i.startswith('p')])

# Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'
print([i for i in my_fruits if i in basket if i.startswith('b')])
print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])

# Print a (3,3) matrix using list comprehension -> Nested List comprehension
print([[i*j for i in range(1,4)] for j in range(1,4)])

# cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]

print([i*j for i in L1 for j in L2])

#2 ways to traverse a list
# itemwise
l = [1.2,3,4]

L = [1,2,print,type,input]

print(L)

for i in l:
    print(i)

# indexwise
l = [1,2,3,4]
for i in range(0,len(l)):
    print(i)

# Zip
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

l1 = [1,2,3,4]
l2 = [-1,-2,-3,-4]
print(list(zip(l1,l2)))
[i+j for i,j in zip(L1,L2)]

L = [1,2,print,type,input]
# list can contain any kind of object
print(L)

# Disadvantages of Python Lists
# Slow
# Risky usage
# eats up more memory