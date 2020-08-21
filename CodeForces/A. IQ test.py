t = input()
n = int(t)
s = input()
temp = s.split()
numberList = [int(i) for i in temp]
evenIndex = []
oddIndex = []
for i in range(len(numberList)):
    if numberList[i] % 2 == 0:
        evenIndex.append(i)
    else:
        oddIndex.append(i)

if len(evenIndex) == 1:
    print(evenIndex[0] + 1)
elif len(oddIndex) == 1:
    print(oddIndex[0] + 1)
