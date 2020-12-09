import math
K = int(input())

cnt = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        ijgcd = math.gcd(i,j)
        for k in range(1,K+1):
            cnt += math.gcd(ijgcd, k)
print(cnt)