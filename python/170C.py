X,N = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
l,h = X,X
while True:
    if l not in A:
        ans = l
        break
    if h not in A:
        ans = h
        break
    l -= 1
    h += 1
print(ans)