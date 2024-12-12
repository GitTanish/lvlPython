# how to edit items in list
l = [1,2,3,4,5]
l[-1]=500
l[1:4]= [200,300,400]
print(l)

# Deleting items from list
# del,remove,pop,clear
del l
l = [1,2,3,4,5]
#indexing
del l[-1]
del l[1:3]
print(l)

# remove :- no need to indexing
l = [1,2,3,4,5]
l.remove(5)
print(l)

#pop
l.pop(0)
# if indexing is not provided it automatically deletes last element
print(l)

# clear # removes all element from list
l = [1,2,3,4,5]
l.clear()
print(l)

# Operation on lists
#   Arithmetic(+,*)
#   Membership(in, not in)
#   loop

# Arithmetic
#concatenation/merge
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
print(l1+l2)
#multiplication
print(l1*3)

# Membership
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,[5,6]]
l3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(5 in l1)
print(5 not in l1)
print([5,6] in l2)

# Loops
for i in l1:
    print(i,end=" ")

for i in l2:
    print(i,end=" ")

for i in l3:
    print(i,end=" ")
