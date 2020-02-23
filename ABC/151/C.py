N,M = map(int,input().split())
cnt_ac = 0
cnt_wa = 0

aced_state = [False for i in range(N+1)]
wa_state = [0 for i in range(N+1)]

for i in range(M):
    p,s = map(str,input().split())
    p = int(p)
    if aced_state[p] == True:
        continue
    else:
        if s == "AC":
            cnt_ac += 1
            cnt_wa += wa_state[p]
            aced_state[p] = True
        else:
            wa_state[p] += 1

print(cnt_ac,cnt_wa)
