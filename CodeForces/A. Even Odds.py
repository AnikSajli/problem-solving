import math
t = input()
temp = t.split()
n = int(temp[0])
k = int(temp[1])

oddLimit = math.ceil(n/2)
if (k <= oddLimit):
    print(k*2-1)
if (k > oddLimit):
    pos = k - oddLimit
    print(pos*2)
