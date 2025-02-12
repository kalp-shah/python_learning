##final=0
##num=1
##for no in range(1,21):
##    final=num+final
##    num=final-num
##    print(final)
##
##n1 = 0
##n2 = 0
##for number in range(1,21):
##    if number == 1:
##        n1 = 1        
##    if number == 2:
##        n2 = 1        
##    n3 = n1 + n2
##    n1 = n2
##    n2 = n3
##    print(n3)
##
##a = 0
##c = 1
##for no in range (a, 20, c):
##    print(a)
##    a = a + c
##    c = a + c


fno = 1
sno = 1
print(fno)
print(sno)
for no in range(1,19):
    sum = fno +sno
    print(sum)
    fno = sno
    sno = sum
