def sum1(n):
    return (n * (n + 1)) // 2


def sum2(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + i
    return sm


t = int(input("Enter no. of testcases : "))
while t:
    n = int(input("Enter integer inputs : "))
    print("sum1 output using iterative method {}".format(sum1(n)))
    print("sum2 output using formula {}".format(sum2(n)))
    t-=1
