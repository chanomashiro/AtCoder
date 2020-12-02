N,K = map(int,input().split())
snuke_okashi_motteru = set()
for i in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    [snuke_okashi_motteru.add(a) for a in A]
print(N - len(snuke_okashi_motteru))
