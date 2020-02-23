import itertools

N = int(input())
P = "".join(list(map(str,input().split())))
Q = "".join(list(map(str,input().split())))

tmp = [i for i in range(1,N+1)]
nums = []
for i in itertools.permutations(tmp):
    _ = []
    for j in i:
        _.append(str(j))
    nums.append("".join(_))

print(abs(nums.index(P) - nums.index(Q)))