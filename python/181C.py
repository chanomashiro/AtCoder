N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (Y[i] - Y[j]) == 0 and (Y[i] - Y[k]) == 0:
                print("Yes")
                exit()
            elif (Y[i] - Y[j]) == 0 or (Y[i] - Y[k]) == 0:
                continue
            elif ((X[i] - X[j]) / (Y[i] - Y[j])) == ((X[i] - X[k]) / (Y[i] - Y[k])):
                print("Yes")
                exit()
print("No")