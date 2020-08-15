t = input()
n = int(t)
xCoordinate = []
yCoordinate = []
zCoordinate = []

for i in range(n):
    vector = input()
    temp = vector.split()
    forceVector = [int(i) for i in temp]
    xCoordinate.append(forceVector[0])
    yCoordinate.append(forceVector[1])
    zCoordinate.append(forceVector[2])

if (sum(xCoordinate) == 0) and (sum(yCoordinate) == 0) and (sum(zCoordinate) == 0):
    print("YES")
else:
    print("NO")
