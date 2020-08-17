import math
t = input()
temp = t.split()
n = int(temp[0])
m = int(temp[1])

divident = math.floor(n/2)
modulus = (n%2)
minSteps = divident+modulus
modulus2 = minSteps % m

if m>n:
    result = -1

elif modulus2 == 0:
    result = minSteps

else:
    result = minSteps + (m-modulus2)
print(result)
