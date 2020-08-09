word = input()
ifHello = ''
lCount = 0
hCount = 0
eCount = 0
oCount = 0

for letter in word:
    if (letter == 'h') and (letter not in ifHello):
        ifHello = ifHello + letter
        hCount = 1
    elif (letter == 'e') and (letter not in ifHello) and (hCount == 1) :
        ifHello = ifHello + letter
        eCount = 1
    elif (letter == 'l') and (lCount <= 1) and (eCount == 1):
        lCount += 1
        ifHello = ifHello + letter
    elif (letter == 'o') and (letter not in ifHello) and (lCount == 2):
        ifHello = ifHello + letter

if (ifHello == 'hello'):
    print('YES')
else:
    print('NO')
