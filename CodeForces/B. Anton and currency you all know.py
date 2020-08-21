t = input()
digits = [int(i) for i in t]
flag = 0
length = len(digits)
lastDigit = digits[length-1]

for i in range(length-1):
    if (digits[i] % 2 == 0) and (digits[i] < lastDigit):
        digits[length-1], digits[i] = digits[i], digits[length-1]
        flag = 1
        break
j = length - 2
while (j >= 0) and (flag == 0):
    if (digits[j] % 2 == 0) and (digits[j] > lastDigit):
        digits[length-1], digits[j] = digits[j], digits[length-1]
        flag = 1
        break
    j -= 1

if flag == 0:
    print(-1)
else:
    for digit in digits:
        print(digit,end="")
