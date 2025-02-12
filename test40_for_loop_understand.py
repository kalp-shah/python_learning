fno = 1
sno = 1
print(fno)
print(sno)
for no in range(1,19):
    sum = fno +sno
    print(sum)
    fno = sno
    sno = sum
