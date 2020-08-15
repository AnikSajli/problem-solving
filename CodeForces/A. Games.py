t = input()
n = int(t)
homeJersey = []
awayJersey = []
count = 0
for i in range(n):
    color = input()
    temp = color.split()
    homeJersey.append(temp[0])
    awayJersey.append(temp[1])

for i in range(n):
    for j in range(n):
        if homeJersey[i] == awayJersey[j]:
            count += 1
print(count)
