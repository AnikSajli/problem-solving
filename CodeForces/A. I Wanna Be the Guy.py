t = input()
levels = int(t)
levelList = []
x = input()
temp = x.split()
for i in range(1,len(temp)):
    levelList.append(int(temp[i]))

y = input()
temp = y.split()
for i in range(1,len(temp)):
    levelList.append(int(temp[i]))

flag = 0

for i in range(1,levels+1):
    if i not in levelList:
        flag = 1

if flag == 0:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
