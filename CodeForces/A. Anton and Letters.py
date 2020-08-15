t = input()
letterList = []
for i in t:
    if (i != '{') and (i != '}') and (i != ',') and (i != ' '):
        letterList.append(i)
dictionary = dict()
for i in letterList:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
print(len(dictionary))
