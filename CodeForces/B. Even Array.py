t = input()
testcase = int(t)

for i in range(testcase):
    t = input()
    n = int(t)
    s = input()
    temp = s.split()
    numbers = [int(i) for i in temp]
    mismatch = 0
    indexEven = 0
    arrayEven = 0
    for i in range(n):
        if (i % 2) != (numbers[i] % 2):
            mismatch += 1
            if (i % 2) == 0:
                indexEven += 1
            if (numbers[i] % 2) == 0:
                arrayEven += 1

    if (indexEven == arrayEven):
        print(int(mismatch/2))
    else:
        print(-1)
