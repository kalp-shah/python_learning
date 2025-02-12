no=int(input("enter a number: "))
sum = 0
while no != 0:
    dig = no % 10
    sum = sum + dig
    no = no // 10
print(sum)
