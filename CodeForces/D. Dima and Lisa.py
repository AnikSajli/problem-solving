import math
n = int(input())

def isPrime(number):
    flag = True
    if (number == 1):
        return False
    for i in range(2,math.floor(math.sqrt(number))+1):
        if (number % i) == 0:
            flag = False
    if (flag):
        return True
    else:
        return False

if (isPrime(n)):
    print(1)
    print(n)
elif (isPrime(n-2)):
    print(2)
    print(n-2,2)
elif (isPrime(n-3)):
    print(n-3, 3)

else:
    flag2 = True
    i = 3
    while (i <= n):
        j = 3
        while (j <= n):
            if (isPrime(i) and isPrime(j) and isPrime(n-i-j)):
                if (i+j+(n-i-j)) == n:
                    flag2 = False
                    print(3)
                    print(i,j,n-i-j)
                    break
            j += 2
        i+= 2
        if (flag2 == False):
            break
