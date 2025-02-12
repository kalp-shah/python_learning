m = int(input("enter num: "))
n = int(input("enter power: "))
ans = 1
for no in range(1,n+1):
    ans = ans * m
print("ans is: ", ans)
