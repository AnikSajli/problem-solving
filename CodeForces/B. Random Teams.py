import math
t = input()
temp = t.split()
participant = int(temp[0])
team = int(temp[1])

largestTeam = participant - (team-1)
maxPair = (largestTeam * (largestTeam - 1)) / 2
commonLeast = math.floor(participant/team)
remainder = participant % team
minPair = 0
minPair = minPair + (((commonLeast+1)*commonLeast)/2)*remainder
minPair = minPair + (((commonLeast-1)*commonLeast)/2)*(team - remainder)

print(int(minPair), int(maxPair))
