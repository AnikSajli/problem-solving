import math
t = input()
temp = t.split()
n = int(temp[0])
k = int(temp[1])
found = False
count = 0
smallFactors = []
bigFactors = []
result = None
for i in range(1,math.floor(math.sqrt(n))+1):
    if (n % i == 0):
        smallFactors.append(i)
        if(i != math.ceil(math.sqrt(n))):
            bigFactors.append(n/i)

if (len(smallFactors)+len(bigFactors) < k):
    print(-1)
else:
    if (k <= len(smallFactors)):
        print(int(smallFactors[k-1]))
    else:
        bigFactors.reverse()
        print(int(bigFactors[k - len(smallFactors) -1]))
