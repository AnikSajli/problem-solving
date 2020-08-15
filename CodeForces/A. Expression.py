t = input()
a = int(t)
t = input()
b = int(t)
t = input()
c = int(t)

case1 = a*b*c
case2 = a+b+c
case3 = (a*b)+c
case4 = (a+b)*c
case5 = a*(b+c)
case6 = a+(b*c)

caseList = []
caseList.extend((case1,case2,case3,case4,case5,case6))

maximum = max(caseList)
print(maximum)
