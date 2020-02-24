N = int(input())
kuku = []
for i in range(1,10):
    for j in range(i,10):
        kuku.append(i*j)
kuku = set(kuku)
if N in kuku:
    print("Yes")
else:
    print("No")
