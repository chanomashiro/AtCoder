S = input()
z = S[:(len(S)-1)//2]
k = S[((len(S)+3)//2)-1:]
if z == z[::-1] and k == k[::-1] and S == S[::-1]:
    print("Yes")
else:
    print("No")