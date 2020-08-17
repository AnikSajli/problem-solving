t = input()
temp = t.split()
n = int(temp[0])
m = int(temp[1])
k = int(temp[2])
armyList = []
friendCount = 0

for i in range(m+1):
    s = input()
    integer = int(s)
    armyList.append(integer)

def compareBits(a,b):
    bitCount = 0
    for i in range(0,32):
        if ((a >> i) & 1) != ((b >> i) & 1):
             bitCount += 1
    return bitCount

for i in range(m):
    bitCount = compareBits(armyList[i],armyList[m])
    if (bitCount <= k ):
        friendCount += 1

print(friendCount)
