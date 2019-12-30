A,B = map(int,input().split())
a,b = A,B
while True:
    if a > b:
        b += B
    elif a < b:
        a += A
    if a == b:
        print(a)
        break