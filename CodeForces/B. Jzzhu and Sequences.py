import math
t = input()
s = input()
temp = t.split()
List = [int(i) for i in temp]
f1 = List[0]
f2 = List[1]
f3 = f2 - f1
f4 = -f1
f5 = -f2
f6 = -f3
n = int(s)
x = math.pow(10,9) + 7

modulus = n%6

if modulus == 1:
    fn = f1
elif modulus == 2:
    fn = f2
elif modulus == 3:
    fn = f3
elif modulus == 4:
    fn = f4
elif modulus == 5:
    fn = f5
elif modulus == 0:
    fn = f6

print(int(fn%x))
