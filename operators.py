#Operators

#Arithmetic
print(5+6)
print(1-6)
print(1/6)
print(5*2)
print(5//2) #int division
print(5**2) # 5^2 #power operator

#relational operators
print(4>5)
print(4<5)
print(4>=5)
print(4<=5)
print(4==4)
print(4!=5)

#Logical Operator
print(1 and 0)
print(1 or 0)
print(not 1)

#BitWise Operator
print(2 & 3) # bitwise and :- 010&110=010 =>2
print(2|3)   # bitwise or :- 010 or 110=110 => 3
print(2 ^ 3) # bitwise xor:- 010 xor 110 =100 => 1
print(~3)    # bitwise not not(110)=001 #basically 2's compliment
print(4>>2)  # left shift
print(4<<2)  # right shift

# Assignment Operators
# =
# a = 2
a = 2
a += 2
print(a)

# Membership Operator
#in/not in

print('D' in 'Delhi') # Wow!
print('M' not in ',Melhi') # Wow!
print(1 in [2,3,4,5,6])

a = input("Find a letter if it exist in the list:")
b = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
print(a in b)

#Program - Find the sum of a 3 digit number entered by the user
#Modulus magic
# xyz
number = int(input("Enter 3 digit number: "))
a = number%10 # z extracted
number = number//10 # converting xyz to xy with int division
b = number%10 # extracted y from xy
number = number//10 # converting  xy to x
print(number+b+a) # now x+y+z