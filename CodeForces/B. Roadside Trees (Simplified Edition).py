t = input()
n = int(t)
treeList = []
time = 0
for i in range(n):
    s = input()
    temp = int(s)
    treeList.append(temp)
time = treeList[0] + 1
for i in range(1, n):
    if treeList[i - 1] > treeList[i]:
        time = time + (treeList[i-1] - treeList[i]) + 1 + 1
    else:
        time = time + 1 + (treeList[i] - treeList[i-1]) + 1

print(time)
