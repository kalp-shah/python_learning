no=int(input("enter a number: "))
rev = 0
while no != 0:
    dig = no % 10
    no = no // 10
    rev = rev * 10 + dig
print(rev)
