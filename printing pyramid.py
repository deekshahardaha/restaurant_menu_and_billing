#printing pyramid
n = int(input())
f=1
for i in range(1,n+1):
    print(("*5"*i).center(2*n))
    print(" "*(n-i)+"* "*i+" "*(n-i))

