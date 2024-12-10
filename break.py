#check whether the number is prime or not


lower = int(input("Enter lower limit: "))
upper = int(input("enter upper limit: "))

if lower>1:
    print("Here's the list of prime numbers within the range")
    for i in range(lower,upper+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")

else:
    print("enter lower range greater than 1")

# Continue
for i in range(1,10):
    if i==5:
         continue #skips the iteration
    print(i,end=" ")