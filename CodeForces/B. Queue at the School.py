t = input()
temp = t.split()
n = int(temp[0])
time = int(temp[1])
s = input()
queue = list(s)
temporaryQueue = queue.copy()

for j in range(time):
    for i in range(1,n):
        if (queue[i] == 'G') and (queue[i-1] == 'B'):
            temporaryQueue[i-1],temporaryQueue[i] = temporaryQueue[i], temporaryQueue[i-1]
    queue = temporaryQueue.copy()

for i in queue:
    print(i,end = "")
