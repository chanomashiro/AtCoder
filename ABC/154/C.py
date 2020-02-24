N = int(input())
A = len(set(list(map(str,input().split()))))
if N == A:
    print("YES")
else:
    print("NO")