def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    prod = a * b
    return prod // gcd(a, b)


t = int(input())
while t:
    n, m = map(int,input().split())
    print("gcd={} lcm={}".format(gcd(n, m), lcm(n, m)))
    t = t - 1
