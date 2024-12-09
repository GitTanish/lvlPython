# Program 1

# login program and indentation
# email-> sample.mail@gmail.com
# password -> 1234
# = assignment operator and == is equal
email = input("enter email: ")
password = input("Enter Password: ")
if 'sample.mail@gmail.com' in email and password == '1234':
    print('Valid')
elif 'sample.mail@gmail.com' in email and password != '1234':
    print('Enter a valid password')
    password=input("Re-enter correct password: ")
    if password == '1234':
        print('Congratulation Num Num')
    else:
        print('*sigh* YOU ARE WRONG')
else:
    print('Not valid')