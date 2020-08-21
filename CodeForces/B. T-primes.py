import math
t = '3'
n = int(t)
s = '4 5 6'
temp = s.split()
numberList = [int(i) for i in temp]
print(numberList)

for i in range(0,n):
    count = 0
    squareRoot = math.floor(math.sqrt(numberList[i]))
    print(squareRoot)
    for j in range(2, squareRoot):
        print(numberList[i])
        print(count)
        if (numberList[i] % j == 0):
            if (numberList[i]/j == j):
                count = count + 1
            else:
                count += 2
            print("Count:",count)
    if count == 2:
        print('YES')
    else:
        print('NO')
