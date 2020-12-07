A = [list(map(int,input().split())) for i in range(3)]
state = [[False for i in range(3)] for j in range(3)]
dic = {}
for i, l in enumerate(A):
    for j, a in enumerate(l):
        dic[str(a)] = [i,j]

N = int(input())
for _ in range(N):
    b = int(input())
    if str(b) in dic:
        state[dic[str(b)][0]][dic[str(b)][1]] = True

ans = False
for s in state:
    if s.count(True) == 3:
        ans = True
for i in range(3):
    cnt = 0
    for s in state:
        if s[i] == True:
            cnt += 1
    if cnt == 3:
        ans = True
if state[0][0] == True and state[1][1] == True and state[2][2] == True:
    ans = True
if state[2][0] == True and state[1][1] == True and state[2][0] == True:
    ans = True

if ans:
    print("Yes")
else:
    print("No")


