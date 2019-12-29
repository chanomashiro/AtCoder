X = int(input())
while True:
    sosuu = True
    for i in range(2,X//2):
        if X % i == 0:
            X += 1
            sosuu = False
            break
    if sosuu:
        print(X)
        exit()
