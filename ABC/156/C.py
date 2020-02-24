N = int(input())
X = list(map(int,input().split()))
min_tairyoku_sum = float("inf")
for i in range(1,101):
    tairyoku_sum = 0
    for x in X:
        tairyoku_sum += (x - i) ** 2
    min_tairyoku_sum = min(tairyoku_sum, min_tairyoku_sum)
print(min_tairyoku_sum)