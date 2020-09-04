t = '{b, a, b, a}'
letterList = []
for i in t:
    if (i != '{') and (i != '}') and (i != ',') and (i != ' '):
        if (i not in letterList):
            letterList.append(i)

print(len(letterList))
