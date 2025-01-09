# strings are a sequence of unicode characters
s = 'hello'
s = "hello"
s = '''hello''' #used for multiline strings
print(s)
s = str('hello')
print('''Fyodor dostoevesky's novel,"WHITE NIGHTS" is amazing''')

#positive Indexing #basically indexing starts from '0' and moves to the righthand side in increasing order
i = 'hello world'
print(i[6])

#Negative indexing # python automatically assigns '-1' to the last element, '-2' to the second last element and so on
# right to left
i = 'hello world'
print(i[-11])

# Slicing
s = 'hello world'
print(s[0:4])
print(s[0:11:2])
print(s[6:0:-1])
#string reversal
print(s[::-1])

print(s[-5:])
print(s[0:5][::-1]) #olleh
print(s[-11:-6]) #hello using negative indexing
print(s[-1:-6:-1])# world reversal

# editing and deleting string
s = 'hello world'
#s[0]='H' #not allowed
# Python strings are immutable
# so strings cannot be moddified
del s# possible but del s[-1:-5:-2]


#Operations on strings
# Arithmetic Operators - +,* only
# Relational Operators
# Logical Operators
# Loops on Strings
# Membership Operations

# Arithmetic Operators
print('delhi'+' mumbai')
print('delhi '*5)

# Relational Operators
print('delhi'=='mumbai')
print('mumbai'>'pune') #false
# strings are being compared lexiographically i.e. ascii value(ascii chart)

# Logical operator
# interview shenanigans
print('hello' and 'world')
print('hello' or 'world')
print('' and 'world') # empty strings are false in python
print('' or 'world')
print(not '') #true
print(not 'world') #false

# Loops on strings
for i in 'hello':
    print(i,end=' ')
for i in 'delhi':
    print('mumbai')

print('D' in 'Delhi')

# Common Functions of string
# len
# max
# min
# sorted

print(len('hello world')) #counts length
print(max('hello world')) # finds maximum  character based on ascii
print(min('hello world')) # ' ' has the lowest ascii
print(sorted('hello world')) # sorts in ascending order based on ascii
print(sorted('hello world',reverse=True))

# Capitalize/Title/Upper/Lower/Swapcase
s = 'hello world'
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
s = 'HeLLo WorLd'
print(s.swapcase()) # upper ko lower, lower ko upper

# Count/find/index
s = 'I am Batman'
print(s.count('a'))
print(s.find('am')) #it won't throw any error even if the character doesn't exist simply return -1
print(s.index('B')) #but it will throw an error if the character doesn't exist

# endswith/startswith
print(s.endswith('an'))
print(s.startswith('an'))

#format
name = 'nitish'
gender = 'male'
print(f"My name is {name}, and I am {gender}")
print('hi my name is {} and i am {}'.format(name,gender))

# isalnum/isalpha/isdigit/isidentifier
# alpha numeric= alphabets+numeric
print(s.isalnum())
#isalpha=only alphabet
s='hellp'
print(s.isalpha())
print(s.isdigit())
print(s.isidentifier())

#split :- breaks the statement word by word and coverts it into a list
print('Hello my name is subaru'.split())
print('Hello my name is subaru'.split('is'))

# join  :- combine words make sentences
print("_".join(['Hello', 'my', 'name', 'is', 'subaru']))

# Replace
print('hi my name is nitish'.replace('nitish','campusx'))

# strip
print('rest                   '.strip())
# The strip method removes leading and trailing characters, not characters in the middle of the string
