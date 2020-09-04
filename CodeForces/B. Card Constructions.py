t = '24'
testcase = int(t)

for i in range(testcase):
    s = input()
    n = int(s)
    temp = n
    sum = 2
    difference = 5
    count = 1
    while(temp == 0) or (temp == 1):
        if (sum > temp):
            sum = sum - difference
            temp = sum
            count -= 1
        sum = sum + difference
        difference += 3
        count += 1
    print(count)
