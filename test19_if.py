a = int(input("First number : " ))
b = int(input("Second number : " ))
c = int(input("third number : " ))
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
input()
