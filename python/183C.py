N,K = map(int,input().split())
T = [list(map(int,input().split())) for i in range(N)]

import itertools
num = [i for i in range(1,N)]
p = itertools.permutations(num)
ans = 0
for v in p:
    time = 0
    current = 0
    for city in v:
        time += T[current][city]
        current = city
    time += T[city][0]

    if time == K:
        ans += 1

print(ans)