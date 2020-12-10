import numpy as np
N = int(input())

divs = []
for i in range(1,int(np.sqrt(N))+1):
    if N % i == 0:
        divs.append(i)
min_div = float("inf")
for i in divs:
    min_div = min(i+(N/i), min_div)
print(int(min_div-2))