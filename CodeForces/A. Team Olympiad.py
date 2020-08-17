t = input()
children = int(t)
List1 = []
List2 = []
List3 = []

value = input()
valueList = value.split()
for i in range(children):
    if (valueList[i] == '1'):
        List1.append(i)
    elif (valueList[i] == '2'):
        List2.append(i)
    elif (valueList[i] == '3'):
        List3.append(i)

len1 = len(List1)
len2 = len(List2)
len3 = len(List3)

maximumTeams = min(len1, len2, len3)
print(maximumTeams)

if maximumTeams>0:
    for i in range(maximumTeams):
        print(List1[i]+1,List2[i]+1,List3[i]+1 )
