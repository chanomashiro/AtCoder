A,B = map(int,input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a / gcd(a, b) * b

print(int(lcm(A,B)))