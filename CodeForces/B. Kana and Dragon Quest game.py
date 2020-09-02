import math
t = input()
testcase = int(t)
for i in range(testcase):
    s = input()
    temp = s.split()
    hitpoint = int(temp[0])
    absorption = int(temp[1])
    lightning = int (temp[2])

    while (hitpoint > 0) and (absorption > 0) and ((math.floor(hitpoint/2) + 10) < hitpoint):
        absorption -= 1
        hitpoint = math.floor(hitpoint/2) + 10

    if (hitpoint <= lightning * 10):
        print("YES")
    else:
        print("NO")
