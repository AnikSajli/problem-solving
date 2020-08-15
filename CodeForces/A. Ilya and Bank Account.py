import math
t = input()
n = int(t)
maximum = n

case1 = math.floor(n/10)
if (case1 > maximum):
    maximum = case1
case2 = (n%10) + math.floor(n/100)*10
if (case2 > maximum):
    maximum = case2
print(maximum)
