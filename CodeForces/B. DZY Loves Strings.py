import operator
from string import ascii_lowercase
s = input()
t = input()
k = int(t)
String = input()
temp = String.split()
number = [int(i) for i in temp]

strlen = len(s)
existingStringValue = 0
dictionary = dict()
index = 0
for i in ascii_lowercase:
    dictionary[i] = number[index]
    index += 1
maxValueKey = max(dictionary.items(), key=operator.itemgetter(1))[0]

j = 1
for letter in s:
    existingStringValue = existingStringValue + dictionary[letter]*j
    j += 1

for i in range(strlen+1, strlen + k +1):
    newStringValue = newStringValue + dictionary[maxValueKey] * i
print(newStringValue + existingStringValue)
