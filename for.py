

for i in range(1,100,2):
    print(i)
for i in range(10,0,-2):
    print(i)

# the current population of a town is 10000.The population of the town is increasing
# at the rate of 10% per year. you have to write a program to find out the
# population at the end of each of the last 10 year

crr_pop =10000

for i in range(10,0,-1):
    print(i, crr_pop)
    crr_pop= crr_pop/1.

# Approach 1 - less efficient
import math

# code for 1/1! + 2/2!.....
n = int(input('enter n: '))
result=0
for i in range(1,n+1):
    result = result+ i/math.factorial(i) #n/n!

print(result)

# Another way of doing this - more efficient
fact = 1
result =0
for i in range(1,n+1):
    fact = fact*i
    result= result+i/fact
print(result)
