t = input()
temp = t.split()
n = int(temp[0])
m = int(temp[1])

pieces = input()
temp = pieces.split()
intList = [int(i) for i in temp]

intList.sort()
result = None
for i in range(m):
    if (i+(n-1) > m-1):
        break
    difference = intList[i+(n-1)] - intList[i]
    if (result is None) or difference < result:
        result = difference
print(result)
