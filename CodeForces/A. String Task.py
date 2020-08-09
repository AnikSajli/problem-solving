word = input()
result = ''
word = word.lower()
for letter in word:
    if (letter == "A") or (letter == "O") or (letter == "Y") or (letter == "E") or (letter == "U") or (letter == "I") or (letter == "a") or (letter == "o") or (letter == "y") or (letter == "e") or (letter == "u") or (letter == "i") :
        word = word.replace(letter,'')

for letter in word:
    result = result + '.' + letter
print(result.strip())
