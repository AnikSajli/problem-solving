t = input()
temp = t.split()
n = int(temp[0])
m = int(temp[1])

s = input()
temp = s.split()
List = [int(i) for i in temp]
time = 0
for i in range(m):
    if i == 0:
        time = time + (List[i] - 1)
    elif (List[i] < List[i-1]):
        time = time + (n-List[i-1]) + List[i] 
    elif (List[i] > List[i-1]):
        time = time + (List[i] - List[i-1])
print(time)
