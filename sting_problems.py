# # find the length of a given string without using the len() function
# s = input("Enter a string: ")
# counter = 0
# for i in s:
#     counter+=1
# print(counter)
from itertools import count

# extract username from a given email.
# Eg if the email is xyz@gmail.com
# then username is xyz

# s = input("Enter email: ")
# a = s.index('@')
# print(s[0:a])

# count the frequency of a particular character in a provided string
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

# s = input("Enter a string : ")
# f = input("enter a character to find: ")
# counter =0
# for i in s:
#     if i == f:
#         counter+=1
# print(counter)

# write a program which can remove a particular character from a string
# note strip only removes first and last not middle
# s = input("Enter a string : ").strip()
# f = input("enter a character to remove: ")
#
# print(s.replace(f,''))

# campusx's way but replace is more efficient
# s = input("Enter a string : ").strip()
# f = input("enter a character to remove: ")
#
# result=''
# for i in s:
#     if i != f:
#         result = result+i
# print(result)

# write a program that can check whether a given string is palindrome or not.
# s = input('enter a string: ')
# flag = True
# for i in range(0,len(s)//2):
#     if s[i] != s[len(s) -i -1]:
#         flag=False
#         print('Not a palindrome')
#         break
#
# if flag:
#     print('Palindrome')

# write a program to count the number of words in a string without split()
# s = input('enter a string:')
# L =[]
# temp = ''
# for i in s:
#     if i != ' ':
#         temp=temp+i
#     else:
#         L.append(temp.append(temp))
#         temp=''
# print(L)

# write a python program to convert a string to title case without using the title()
# s = input('enter a string:')
#
# L = []
# for i in s.split():
#     L.append(i[0].upper()+i[1:].lower())
#
# print("I".join(L))

# int to string

number = int(input('Enter the number: '))
digits = '0123456789'
result = ''
while number != 0:
    result = digits[number%10]+result
    number=number//10
print(result)