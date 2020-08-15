t = input()
temp = t.split()
x1 = int(temp[0])
y1 = int(temp[1])
x2 = int(temp[2])
y2 = int(temp[3])

if (x1 != x2) and (y1 != y2) and (abs(x1-x2) != abs(y1-y2)):
    print(-1)

elif (x1 == x2):
    a = abs(y1-y2)
    x3 = x1 + a
    x4 = x2 + a
    y3 = y1
    y4 = y2
    print(x3,y3,x4,y4)

elif (y1 == y2):
    a = abs(x1-x2)
    x3 = x1
    x4 = x2
    y3 = y1 + a
    y4 = y2 + a
    print(x3,y3,x4,y4)

elif (x1 != x2) and (y1 != y2):
    a = abs(x1-x2)
    x3 = x1
    x4 = x2
    y3 = y2
    y4 = y1
    print(x3,y3,x4,y4)
