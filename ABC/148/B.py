N = int(input())
S,T = map(str,input().split())
string = ""
for i in range(N):
    string += S[i]
    string += T[i]
print(string)