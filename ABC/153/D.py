H = int(input())
ans = 0
num_monster = 1
while(H >= 1):
    H //= 2
    ans += num_monster
    num_monster *= 2
print(ans)