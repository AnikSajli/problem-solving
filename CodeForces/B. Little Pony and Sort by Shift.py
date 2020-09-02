t = input()
n = int(t)
s = input()
temp = s.split()
numbers = [int(i) for i in temp]
flag = 0
for i in range(1,len(List)):
    if List[i] < List[i-1]:
        flag++
         j = i
if (flag == 0):
    print(0)
elif(flag > 1):
    print(-1)
elif (flag == 1) and (numbers[n-1] <= numbers[0]):
    print(n-k+1)
