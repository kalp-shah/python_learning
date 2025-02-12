no=int(input("enter a number: "))
no1 = no
sum = 0
while no != 0:
    dig = no % 10
    no = no // 10
    sum = sum  + (dig*dig*dig)
print(sum)
print(no1)
if sum == no1:
    print("Armstrong")
else:
    print("Not Armstrong")

