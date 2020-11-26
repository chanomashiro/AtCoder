n = list(map(int,list(input())))
mod = [nn%3 for nn in n]

def solve(n):
    if sum(n) % 3 == 0:
        return 0
    if sum(n) % 3 == 1:
        if 1 in mod and len(mod) != 1:
            return 1
        elif mod.count(2) >= 2 and len(mod) != 2:
            return 2
    if sum(n) % 3 == 2:
        if 2 in mod and len(mod) != 1:
            return 1
        elif mod.count(1) >= 2 and len(mod) != 2:
            return 2
    return -1

print(solve(n))