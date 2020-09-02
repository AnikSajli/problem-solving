s1 = '0 3 6'
temp = s1.split()
r1 = [int(i) for i in temp]

s2 = '5 0 5'
temp = s2.split()
r2 = [int(i) for i in temp]

s3 = '4 7 0'
temp = s3.split()
r3 = [int(i) for i in temp]

sum = (r1[1] + r1[2] + r2[0] + r2[2] + r3[0] + r3[1]) / 2
r1[0] = int(sum - (r1[1] + r1[2]))
r2[1] = int(sum - (r2[0] + r2[2]))
r3[2] = int(sum - (r3[0] + r3[1]))
