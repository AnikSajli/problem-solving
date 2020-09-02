s = input()
temp = s.split()
twoDigitCount = int(temp[0])
threeDigitCount = int(temp[1])
fiveDigitCount = int(temp[2])
sixDigitCount = int(temp[3])
bigNumberCount = min(twoDigitCount, fiveDigitCount, sixDigitCount)

twoDigitCount = twoDigitCount - bigNumberCount
fiveDigitCount = fiveDigitCount - bigNumberCount
sixDigitCount = sixDigitCount - bigNumberCount

smallNumberCount = min(threeDigitCount, twoDigitCount)

print(256*bigNumberCount + 32*smallNumberCount)
