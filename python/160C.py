K,N = map(int,input().split())
A = list(map(int,input().split()))
diff = []
for i in range(len(A)-1):
    diff.append(A[i+1] - A[i])
diff.append((K+A[0]) - A[-1])
print(sum(diff) - max(diff))