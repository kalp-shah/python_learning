no=int(input("enter a number: "))
no1 = no
sum = 0
while no != 0:
    dig = no % 10
    no = no // 10
    sum = sum * 10 + dig
print(sum)
print(no1)
if sum == no1:
    print("Palindrome")
else:
    print("Not Palindrome")

