t = input()
n = int (t)
for i in range(n):
    word = input()
    if len(word) > 10:
        middle = str(len(word)-2)
        output = word[0] + middle + word[len(word)-1]
        print(output)
    else:
        print(word)
