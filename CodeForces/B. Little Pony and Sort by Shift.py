t = input()
n = int(t)
s = input()
temp = s.split()
numbers = [int(i) for i in temp]
newList = []

def checkIfSorted(List):
    j = 0
    for i in range(1,len(List)):
        if List[i] < List[i-1]:
            j = 1
    if j == 0:
        return True
    if j == 1:
        return False

if checkIfSorted(numbers) == True:
    print(0)
else:
    minimum = min(numbers)
    minIndex = numbers.index(minimum)
    if (numbers[n-1] == minimum) and (numbers[0] == minimum):
        minIndex = n -1
    for i in range(minIndex,n):
        newList.append(numbers[i])
    for i in range(minIndex):
        newList.append(numbers[i])

    isSortable = checkIfSorted(newList)

    if (isSortable == True):
        print(n - minIndex)
    else:
        print(-1)
