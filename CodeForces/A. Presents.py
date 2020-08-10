t = input()
n = int(t)
friends = input()
List = friends.split()
friendList = []

for friend in List:
    temp = int(friend)
    friendList.append(temp)

for j in range(1,n+1):
    for index in range(n):
         if friendList[index] == j:
             print(index+1)
