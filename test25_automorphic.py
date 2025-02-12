a = int(input("Enter Number : "))
b = a * a
if a < 10:
    c = b % 10
else:
    c = b % 100
if a == c:
    print("Automorphic")
else:
    print("Not Automorphic")
input()
