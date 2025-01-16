#If 2 newborn rabbits are put in a pen, How many rabbits will be in the pen after 1 year
#Assume that rabbits always produce one male and one female offspring
#Can reproduce once every month
#Can reproduce once they are one month old
#Never Die

# def fib(m):
#     if m == 0 or m ==1:
#         return 1
#     else:
#         return fib(m-1) + fib(m-2)
# print(fib(36))

# This piece of code is very inefficient

# Memoization
def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m]=memo(m-1,d) + memo(m-2,d)
        return  d[m]


d = {0:1,1:1}
print(memo(48,d))