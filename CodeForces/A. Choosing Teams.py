import math
t = input()
temp = t.split()
n = int(temp[0])
k = int(temp[1])

s = input()
temp = s.split()
numbers = [int(i) for i in temp]

allowedNumber = 5-k
count = 0

for number in numbers:
    if number <= allowedNumber:
        count += 1
print(math.floor(count/3))
