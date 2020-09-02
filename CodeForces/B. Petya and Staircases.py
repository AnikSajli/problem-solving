t = input()
temp = t.split()
n = int(temp[0])
m = int(temp[1])
s = input()
temp = s.split()
blockedStairs = [int(i) for i in temp]
blockedStairs.sort()
maximum = 0
count = 0

for i in range(1,len(blockedStairs)):
    if (blockedStairs[i] == blockedStairs[i-1] + 1):
        count += 1
    if (blockedStairs[i] != blockedStairs[i-1] + 1) or (i == len(blockedStairs)-1):
        if (count > maximum):
            maximum = count
        count = 0

if (blockedStairs[0] == 1) or (blockedStairs[n-1] == n):
    print("NO")
elif (maximum + 1) <= 2:
    print("YES")
else:
    print("NO")
