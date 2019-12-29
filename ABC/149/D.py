N, K = map(int,input().split())
R, S, P = map(int,input().split())
T = list(str(input()))

can_use = []
score = 0

def get_score(forwin):
    if forwin == "r":
        score = R
    elif forwin == "s":
        score = S
    elif forwin == "p":
        score = P
    return score

def can_use_hand(forwin):
    if forwin == "r":
        hands = ["s", "p"]
    elif forwin == "s":
        hands = ["r", "p"]
    elif forwin == "p":
        hands = ["r", "s"]
    return hands

for i in range(N):
    if T[i] == "r":
        forwin = "p"
    elif T[i] == "s":
        forwin = "r"
    elif T[i] == "p":
        forwin = "s"
    
    if len(can_use) < K:
        score += get_score(forwin)
        can_use.append(can_use_hand(forwin))
    else:
        can_use_hands = can_use[-K]
        if forwin in can_use_hands:
            score += get_score(forwin)
            can_use.append(can_use_hand(forwin))
        else:
            score += 0
            can_use.append(["r","s","p"])
print(score)


