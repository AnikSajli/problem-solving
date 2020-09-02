s = input()
temp = s.split()
dictionary = dict()
for i in range(len(s)):
    if s[i] not in dictionary:
        dictionary[s[i]] = 1
    else:
        dictionary[s[i]] += 1

oddLetter = 0

for i,j in dictionary.items():
    if (j % 2 != 0):
        oddLetter += 1

if oddLetter <= 1:
    print("First")
elif (oddLetter % 2) == 0:
    print("Second")
else:
    print("First")
