# Sets

# A set is an unordered collection of items. Every set element is unique (no duplicates)
# and must be immutable (cannot be changed).
# However, a set itself is mutable.
# We can add or remove items from it.
# Sets can also be used to perform mathematical set operations like union,
# intersection, symmetric difference, etc.
#
# Characterstics:
# - Unordered
# - Mutable
# - No Duplicates
# - Can't contain mutable data types
# - also set cannot be nested

s = set()
#set and dictionary share similar syntax so if s = {} it will be a dict by default
# 1d and 2d, exist and 2d doesn't
s = {1,2,3}
print(s)
# hetero
s3 = {1,'hello',4.5,True,(1,2,3,4)} # you cannot have duplicates in sets and python treats True as 1 so it won't be printed
# sets undergo hashing
print(s3)
# using type conversion
s4 = set([1,2,3,4])
print(s4)
s5 = {1,2,2,3,4,4,5}
print(s5)
# set cannot have mutable elements so a tuple can be in set but a list cannot be
# also set is unordered
s1 = {1,2,3}
s2 = {3,2,1}
print(s1==s2) # so it just compares the element not their order

# Accessing Items
# sets doesn't have indexing and slicing
# sets can't be edited
# but items can be added or deleted in sets
s = {1,2,3,4}
s.add(5)
print(s)
# update - multiple items can be added using update
s.update ([6,7,8])
print(s)

# deleting items
# del - whole set gets deleted
del s
# discard - deletes particular element
s = {1,2,3,4}
s.discard(3) # if the item doesn't exist discard won't throw any error
print(s)
# remove
s.remove(1) # but if the item doesn't exist remove will throw an error
# otherwise they work similarly

# pop # random deletion
s.pop()
print(s)

# clear
s.clear() # empties the whole set
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# Union(|)
print(s1 | s2) # merges item from both the sets
# intersection (&)
print(s1 & s2)
# Difference (-)
print(s1-s2) # s1 ke wo items jo s2 mein present nahi hai
# Symmetric Difference (^) # everything will be printed except same values
print(s1^s2)
# Membership test
print(1 in s1)
print(1 not in s1)
# iteration
for i in s1:
    print(i)

# len/sum/min/max/sorted
s = {3,1,4,5,2,7}
len(s)
print(s)
sum(s)
print(s)
min(s)
print(s)
max(s)
print(s)
print(sorted(s,reverse=True))

# union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# s1 | s2
s1.union(s1)

s1.update(s2)
print(s1)
print(s2)

# intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.intersection(s2)

s1.intersection_update(s2)
print(s1)
print(s2)

# Difference/ difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.difference(s2)

s1.difference_update(s2)
print(s1)
print(s2)

# symmetric_difference/symmetric_difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.symmetric_difference(s2)

s1.symmetric_difference_update(s2)
print(s1)
print(s2)
# isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {7,8,5,6}

print(s1.isdisjoint(s2)) # if any common element is present then False

s1 = {1,2,3,4,5}
s2 = {3,4,5}

s1.issuperset(s2)  # if a set is a subset of the first subset

# copy
s1 = {1,2,3}
s2 = s1.copy()

print(s1)
print(s2)

### Frozenset
# Frozen set is just an immutable version of a Python set object
# create frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

print(fs1 | fs2)
# what works and what does not
# works -> all read functions
# doesn't work -> write operations i.e add,update etc

# when to use
# 2d sets
fs = frozenset([1,2,frozenset([3,4])])

# set comprehension
print({i for i in fs})

print({i**2 for i in range(1,11) if i>5})
