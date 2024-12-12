#Lists
# 1) what are list?
# List is a data type where you can store multiple items under 1 name.
# More technically, lists act like dynamic arrays which means you can add more items on the fly.

# 2) Lists Vs Arrays
# Fixed Vs Dynamic Size
# Convenience -> Heterogeneous #store multiple data types
# Speed of Execution -> slow speed as compared to array
# Memory -> list takes more space compared to arrays
# 3) Characteristics of a list
# 4) How to create a list
# 5) Access items from a list
# 6) Editing items from a list
# 7) Deleting items from a list
# 8) Operations on Lists
# 9) Functions on Lists

# List doesn't store like array instead it stores in different blocks of memories and the reference is stored with them
# similar to a linked list from C or C++
# id() -> shows the memory address
a =2
print(id(2))

L = [1,2,3]

print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))

# Characteristics of a List

# Ordered
# Changeble/Mutable
# Heterogeneous
# Can have duplicates
# are dynamic
# can be nested [1,2,[3,45]]
# items can be accessed
# can contain any kind of objects in python
L = [1,2,3]
l1 = [3,2,1]
print(L==l1) # false because both lists are not same

# Creating a list
# Empty
# 1D
# 2D
# 3D
# heterogenous
# using type conversions

print([])
print([1,2,3,4,5]) # 1d and homogenous
print([1,2,3,[4,5]]) # heterogenous
print([1,2,[3,[4,5]]]) # 3d list still hetero
print(list('hello')) # using type conversion to create a list

# how to fetch item from list
# Indexing
L = [1,2,3,4,5]
#positive
print(L[0])
#negative
print(L[-5])
# For 2D list
L = [1,2,3,[4,5]]
print(L[-1][-2]) # through negative
print(L[3][0])
# For 3D list
L = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(L[1][0][0])
print(L[0][0][1])

#Slicing
L=[1,2,3,4,5,6]
print(L[0:3])


#append
L = [1,2,3,4,5]
L.append(True) # append takes only one argument that's why extend
print(L)
L = [1,2,3,4,5]
L.extend('delhi')
print(L)
L=[1,2,3,4,5]
L.insert(2,200)
print(L)