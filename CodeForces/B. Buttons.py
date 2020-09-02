t = input()
n = int(t)
click = 0
for i in range(1,n):
    click = click + (n-i)*i

print(click + n)
