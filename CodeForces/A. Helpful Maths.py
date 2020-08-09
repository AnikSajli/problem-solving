t = input()
numberList = []
result = ''
for char in t:
    if char != '+':
        numberList.append(char)
numberList.sort()
for number in numberList:
    result = result + number + '+'
print(result[:len(result)-1])
