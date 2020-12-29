N = int(input())
cnt = 0
for i in range(1, N+1):
    oc = oct(i)
    if "7" not in str(i) and "7" not in oc:
        cnt += 1
print(cnt)