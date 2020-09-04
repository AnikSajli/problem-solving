t = input()
temp = t.split()
n = int(temp[0])
x = int(temp[1])
s = input()
temp = s.split()
arr = [int(i) for i in temp]
arr.sort()
count = 0
for i in range(n):
    a = arr[i] ^ x
    if (a in arr):
        index = arr.index(a)
        if (index == i):
            if (index + 1 < n) and (a == arr[index+1]):
                count += 1
        else:
            count += 1
print(int(count/2))
