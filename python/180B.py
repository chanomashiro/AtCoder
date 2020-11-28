import numpy as np

N = int(input())
X = list(map(int,input().split()))

m = sum([abs(x) for x in X])
u = np.sqrt(sum([abs(x) ** 2 for x in X]))
c = max([abs(x) for x in X])

print(m)
print(u)
print(c)