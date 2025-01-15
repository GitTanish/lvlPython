# multiplication is just repeated addition
def multiply(a,b):
    result = 0

    for i in range(b):
        result = result+a
    print(result)

multiply(2,9)

# recursively
def mul(a,b):

    if b==1:
        return a
    else:
        return a+ mul(a,b-1)

print(mul(3,4))
# recursion uses stack and the return value goes from bottom to top

# factorial
def fact(number):
    if number == 1:
        return 1
    else:
        # 5! = 5*4!
        return number * fact(number -1)

print(fact(5))

# palindrome
def palin(text):
    if len(text)<=1:
        print('palindrome')
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print('Not a palindrome')

palin('malayalam')
palin('abba')