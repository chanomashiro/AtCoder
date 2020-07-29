from collections import deque

K = int(input())
que = deque()
runrun = []

for i in range(1,10):
    que.append(i)

def abs01(n):
    if n == 0:
        return [0,1]
    elif n == 9:
        return [8,9]
    else:
        return [n-1,n,n+1]

while True:
    n = que.popleft()
    n_simo1 = int(str(n)[-1])
    nums = abs01(n_simo1)
    for num in nums:
        que.append(n*10+num)
    runrun.append(n)
    if len(runrun) == K:
        print(runrun[-1])
        #print(runrun)
        #print(que)
        exit()
