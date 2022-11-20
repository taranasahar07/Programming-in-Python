def digits(n):
    list = []
    while(n>0):
        digit=n%10
        list.append(digit)
        n=n//10
    return set(list)
n = int(input("Enter a number : "))
nls = digits(n)
print("The digits of number as a set")
for x in nls:
    print(x,end=" ")
