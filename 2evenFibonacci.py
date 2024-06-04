a = 1
b = 2
c = a + b
totalSum = 0
while a < 4000000:
    if a % 2 == 0:
        totalSum += a
    a = b
    b = c
    c = a + b
print(totalSum)