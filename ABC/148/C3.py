import fractions

A,B = map(int,input().split())

def lcm(a, b):
    return a / fractions.gcd(a, b) * b

print(int(lcm(A, B)))