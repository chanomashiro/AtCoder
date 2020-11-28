import numpy as np

N = int(input())

ans = []
for i in range(1,int(np.sqrt(N))+1):
    if N % i == 0:
        ans.append(i)
        ans.append(N // i)

ans = list(set(ans))
ans.sort()
for a in ans:
    print(a)