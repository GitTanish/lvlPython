# if-else examples
# 1.find the min of 3 given numbers
# 2.Menu-driven program

a = int(input("first num: "))
b = int(input("Second num: "))
c = int(input("Third num: "))

if a > b and a > c:
    print('a is largest')
elif b > c and b> a:
    print('b is largest')
elif a==b and a==c:
    print("All numbers are same")
else:
    print('c is largest')

# Menu driven calculator
fnum = int(input('enter 1st number:'))
snum = int(input('enter 2nd number: '))
choice = input("Enter operation(+,-,*,/,%): ")

if choice == '+':
    print(fnum+snum)
elif choice == '-':
    print(fnum-snum)
elif choice == '*':
    print(fnum*snum)
elif choice == '/':
    print(fnum/snum)
elif choice == '%':
    print(fnum%snum)
else:
    print('enter valid choice')
