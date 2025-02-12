sum = 0
for i in range(1, 11):
    fact = 1
    for j in range(i,0,-1):
        fact = fact * j
    if i % 2 == 0:
             sum = sum - 1 / fact
    else:
             sum = sum + 1 / fact
print(sum)             
