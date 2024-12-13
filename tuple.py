# Tuples
# A tuple in Python is similar to a list.
# The difference between the two is that we cannot change the
# elements of a tuple once it is assigned whereas we can change the
# elements of a list.
# In short, a tuple is an immutable list.
# A tuple can not be changed in any way once it is created.
#
# Characteristics
# Ordered
# Unchangeable/ Immutable
# Allows duplicate

# Creating a Tuple
# Accessing items
# Editing items
# Adding items
# Deleting items
# Operations on Tuples
# Tuple Functions

# Creating a Tuple
t1 = ()
print(t1)
# create tuple with single item
t2 =(2) # this is not how single item tuple is made
t2 =(2,) # this is how single item tuple is made
print(t2)
t3 = (1,2,3,4) #homogenous
t4 = (1,2,'hello',False) #heterogenous
t5 = (1,2,(4,5)) # tuple within
print(t3,t4,t5)
# using type conversion
t6 = tuple('hello')
print(t6)

# indexing
print(t3[0])  # positive
print(t3[-4]) # negative

#slicing
print(t3[0:4:2])
print(t3[::-1])
print(t5[2][0]) # 2d element accessing

# adding and editing isn't possible
# deletion is only possible of we delete whole tuple a specific item cannot be deleted in a tuple
del t1

# Operations on Tuples
# + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1+t2)
print(t1*2)
# membership
print(1 in t1)
print(1 not in t1)
# iteration/loops
for i in t1:
    print(i)

# Tuple functions
# len/sum/min/max/sorted
t = (1,2,3,4,5)
print('length of tuple is:',len(t))
print(sum(t))
print(min(t))
print(max(t))
print(sorted(t, reverse = True))
# count
print(t.count(5))

# Difference between Lists and Tuples
# Syntax
# Mutability
# Speed - tuples are faster than list
# Memory - tuple consume less memory
# Built in functionality - list consist of more
# Error prone - list is error prone
a = [1,2,3]
b = a

a.append(4)
print(a)
print(b)

a = (1,2,3)
b = a

a = a + (4,)
print(a)
print(b)
# Usability

# Why use tuple?
# special syntax

# tuple unpacking
a,b,c = (1,2,3)
print(a,b,c)

# a,b = (1,2,3)
# print(a,b) won't work

# swap
a,b = 1,2
a,b=b,a
print(a,b)

a,b,*others = (1,2,3,4)
print(a,b)
print(others)

# zipping tables
a = (1,2,3,4,5)
b = (5,6,7,8)
zip(a,b)
print(list(zip(a,b)))