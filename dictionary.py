# Dictionary
#
#  in Python is a collection of keys values, used to store data values like a map, which,
# unlike other data types which hold only a single value as an element.
# In some languages it is known as map or associative arrays.
# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }
#
# Characteristics:
#
# - Mutable
# - Indexing has no meaning
# - keys can't be duplicated
# - keys can't be mutable items


# empty dictionary
d = {}
print(d)

# 1d dictionary
d = {'name':'krish', 'gender':'male'}
print(d)
d1 =  {(1,2,3):1,'hello':'world'} # both tuples and strings are immutable that's why they can be assigned as keys

# 2d dictionary - JSON
s = {
    'name':'naik',
    'college':'dn',
    'sem':'V',
    'subject':{
        'dsa':60,
        'Ai':80,
        'DWM':50
    }
}
print(s)

# using sequence and dict function
d4 = dict([(1,1),(2,2),('name','nitish'),('age',32)])
print(d4)

# duplicate keys aren't allowed
d5 = {'name':'nitish','name':'rahul'}
# mutable items as keys aren't allowed
d6 = {'name':'nitish',(1,2,3):2}
print(d6)

my_dict = {'name': 'Jack', 'age': 26}
# print(my_dict[0]) wouldn't work because a indexing doesn't work in dictionaries
print(my_dict['name']) # keys can be used for fetching particular elements
my_dict.get('age') # get can also do the job

# adding key-value pair
d4['gender']='male'
print(d4)
d4['weight']='Fat32'
print(d4)
s['subject']['ds'] = 75 # for 2d
print(s)

# remove key-value pair
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
#pop
d.pop(3)
print(d)
# popitem
d.popitem() #deletes the last key value pair
print(d)
# del # deletes the whole dictionary and can also be used for specific deletion
del d['name']
print(d)
#clear
d.clear() #empties the dictionary


### Editing key-value pair
s['sem']=5
print(s)

# dictionary operations
# 1)membership
# 2)Iteration

print('nitish' in s) # but it assumes key not value so to find values use membership with key

# iteration
d = {'name':'nitish','gender':'male', 'age':33}
for i in d:
    print(i,d[i])  #(key,value)


# dictionary functions
# len/sorted/min/max
print(len(d))
print(sorted(d)) # sort all keys in ascending order
print(sorted(d,reverse=True))
print(min(d)) # minimum key on the basis of ascii
print(max(d))

# items/keys/values
# items converts key value pair into tuples
print(d.items())
print(d.keys()) # fetches all the keys
print(d.values()) # fetches all the values

#update # a given dictionary can be updated with a secondary dictionary
d1 = {1:2,3:4,4:5}
d2 = {4:7,6:8}

d1.update(d2)
print(d1)

# dictionary comprehension
# {key:value for vars in iterable}
# print 1st 10 numbers and their squares
print({i:i**2 for i in range(1,11)})
# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print({key:value*0.62 for (key,value) in distances.items()})

# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

print({i:j for (i,j) in zip(days,temp_C)})

# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
print({key:value for (key,value) in products.items() if value>0})

# Nested Comprehension
# print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})