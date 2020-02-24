N = int(input())
count = {}
for _ in range(N):
    s = str(input())
    if s in count.keys():
        count[s] += 1
    else:
        count[s] = 1

max_value = max(count.values())
max_key_list = [kv[0] for kv in count.items() if kv[1] == max_value]
max_key_list.sort()
for key in max_key_list:
    print(key)
