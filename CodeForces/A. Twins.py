numberOfCoins = input()
coins = input()
List = coins.split()
coinList = []

for coin in List:
    integer = int(coin)
    coinList.append(integer)

coinList.sort()
total = sum(coinList)
index = len(coinList)-1
mySum = 0
count = 0
while(True):
    count += 1
    mySum = mySum + coinList[index]
    left = total - mySum
    if left < mySum:
        print(count)
        break
    index -= 1
