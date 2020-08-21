t = input()
temp = t.split()
n = int(temp[0])
l = int(temp[1])
s = input()
temp = s.split()
lamps = [int(i) for i in temp]

maximum = 0
lamps = sorted(lamps)
for i in range(n):
    if i == 0:
        m = (lamps[0] - 0) * 2
    elif i > 0:
        m =  lamps[i] - lamps[i-1]
    if m > maximum:
        maximum = m
    if i == n-1:
        if ((l - lamps[i]) * 2) > maximum:
            maximum = (l - lamps[i]) * 2

result = float(maximum)/2
print('%.10f'%result)
