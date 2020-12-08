N = int(input())
A = list(map(int,input().split()))
count = [0 for i in range(N)]
for i in range(N-1):
    count[A[i]-1] += 1
for c in count:
    print(c)