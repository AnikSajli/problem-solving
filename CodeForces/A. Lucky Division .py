n = input()
number = int(n)

if (number % 4 == 0) or (number % 7 == 0) or (number % 44 == 0) or (number % 77 == 0) or (number % 47 == 0) or (number % 74 == 0) or (number % 444 == 0) or (number % 447 == 0) or (number % 477 == 0):
    print('YES')
else:
    print('NO')
