import math
import numpy as np
A,B,H,M = map(int,input().split())
r = 2 * math.pi * (H/12 + (M/60)/12 - (M/60))

ans = np.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(r))
print(ans)
