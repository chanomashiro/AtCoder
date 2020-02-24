import itertools
import math

N = int(input())
X = []
Y = []
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x); Y.append(y)

num = [i for i in range(N)]
distance_list = []
for perm in itertools.permutations(num):
    prev = None
    distance = 0
    for v in perm:
        if prev is None:
            prev = v
        else:
            distance += math.sqrt((X[prev] - X[v]) ** 2 + (Y[prev] - Y[v]) ** 2)
    distance_list.append(distance)

print(sum(distance_list) / len(distance_list))
