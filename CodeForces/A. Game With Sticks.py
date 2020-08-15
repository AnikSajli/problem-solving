t = input()
dimension = t.split()

n = int(dimension[0])
m = int(dimension[1])
count = 0
while (True):
    numberOfIntersection = n*m
    count += 1
    if numberOfIntersection < 1:
        break
    n = n - 1
    m = m - 1
count -= 1
if count % 2 == 0:
    print('Malvika')
else:
    print('Akshat')
