# baby steps
print("Hello world")
print("print\nnew line\nnew line",9,7.6,True,sep='!')#seperation which is by default=' '
# so sep for separation override

#integer
# 1*10^308 #clocked at this value
print(1e309) #infinite
print(8*10000+4737)

#float/decimal
# 1.7e+308
print(1.2+4.5)

#Boolean
print(True)
print(False)

# String
print('Rick '+'Sanchez C-137')

#complex
print(5+7j)

#List -> C-> Array
print([1,2,3,4,5,6])

#Tuple
print((1,2,3,4))

#sets
print({1,2,3,4,5,6})

#Dictionary
dictionary1 = {'Rick':'Sanchez','Morty':'Smith','Subaru':'Natsuki'} # anti climatic eh
print(dictionary1)

#type
type('Peak')

## Variables
name = 'Android 17'
print(name)

# Important Points(Very important!) :)

# static vs dynamic typing
# don't have to tell the data type while creating a Variable, cause it python and interpreter can understand :)
a =5
# rather than int a =5 (static typing)C,JAVA,C++

# Dynamic Binding
a = 5
print(a)
a = 'Masao'
print(a)
#notice no error cause python support dynamic binding i.e variable can hold any data type

a=1

a,b,c = 1,2,3
print(a,b,c)

x=y=z = 5
print(x,y,z)

#Keywords
#Python keywords are reserved words that have predefined meanings and functions within the language.

#identifier
#Identifiers in Python are names used to identify a variable, function, class, module, or other object. They are essential for giving names to objects so that they can be referenced and manipulated within the code
#Rules for creating identifiers
# You can't start with a digit i.e 1print
# You can use special chars -> _ i.e first_name not first-name
# identifiers cannot be keywords

#User input
# Static vs Dynamic
Name=input("What's your character?")
print("Well "+Name+" let's add 2 numbers")

#take input from users and store them in variable
#input takes by default string
fnum = float(input("Enter first number:")) #Type conversion
snum = float(input("Enter second number:")) #explicit
#add the 2 variables
result = fnum+snum
#print the result
print(result)

# Type conversion
#Implicit vs explicit
print(5+5.6) #INTERPRETER auto converts
print(type(5),type(5.6))

