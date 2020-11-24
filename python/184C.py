a,b = map(int,input().split())
c,d = map(int,input().split())

def solve(a,b,c,d):
    if [a,b] == [c,d]:
        return 0
    if a+b == c+d:
        return 1
    if a-b == c-d:
        return 1
    if abs(a-c)+abs(b-d) <= 3:
        return 1
    if (a+b+c+d) % 2 == 0:
        return 2
    if abs((a+b)-(c+d)) <= 3:
        return 2
    if abs((a-b)-(c-d)) <= 3:
        return 2
    if abs(a-c)+abs(b-d) <= 6:
        return 2
    return 3

print(solve(a,b,c,d))