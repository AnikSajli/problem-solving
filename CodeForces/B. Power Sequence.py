import math
n = int(input())
a = [int(x) for x in input().split()]
a.sort()

k = 1
while (math.pow(k,n) < math.pow(10,10)):
    k += 1
k -= 1
result = None
for i in range(1,k+1):
    cost = 0
    for j in range(1,n+1):
        cost = cost + abs(a[j] - math.pow(i,j))
    result = (result, cost)
    
print(result)
