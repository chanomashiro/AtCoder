A,B,C,D = map(int,input().split())
while True:
    C -= B
    A -= D
    if C <= 0:
        ans = "Yes"
        break
    if A <= 0:
        ans = "No"
        break
print(ans)