import math
def compute(x):
    res =1
    chk =1
    for i in range(2,x+1,2):
        if chk%2==0:
            res+=(i/math.factorial(i))
        else:
            res-=(i/math.factorial(i))
    return res
n =int(input("Enter the value of n : "))
print(compute(n))
