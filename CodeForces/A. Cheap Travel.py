import math
t = '4 4 2 7'
temp = t.split()
n = int(temp[0])
m = int(temp[1])
oneRidePrice = int(temp[2])
mRidePrice = int(temp[3])

mRideCheaper = False

if(mRidePrice < m*oneRidePrice):
    mRideCheaper = True

if (mRideCheaper == False):
    print(n*oneRidePrice)
else:
    divident = math.floor(n/m)
    mod = (n%m)

    cost1 = (mRidePrice * divident) + (mod * oneRidePrice)
    cost2 = (divident + 1) * mRidePrice

    costList = [cost1, cost2]

    print(min(costList))
