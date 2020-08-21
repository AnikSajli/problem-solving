t = input()
temp = t.split()
n = int(temp[0])
m = int(temp[1])
dictionary = dict()

for i in range(m):
    s = input()
    temp = s.split()
    dictionary[temp[0]] = temp[1]
s = input()
line = s.split()

for word in line:
    if len(word) > len(dictionary[word]):
        print(dictionary[word]," ", end = "")
    else:
        print(word," ", end = "")
