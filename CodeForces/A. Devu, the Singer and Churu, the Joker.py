t = input()
temp = t.split()
n = int(temp[0])
d = int(temp[1])
songLenthList = []
songLength = input()
List = songLength.split()
songLenthList = [int(i) for i in List]
devuBreaktime = (n-1)*10
devuTotalTime = devuBreaktime + sum(songLenthList)
churuTime = d - devuTotalTime + devuBreaktime
if (devuTotalTime > d):
    print(-1)
else:
    print(int(churuTime/5))
