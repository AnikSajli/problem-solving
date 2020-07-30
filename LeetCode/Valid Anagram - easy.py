def isAnagram(string1, string2):
        sortedString1 = sorted(string1)
        sortedString2 = sorted(string2)
        if sortedString1 == sortedString2:
            return True
        else:
            return False

result = isAnagram("rat", "car")
print(result)
