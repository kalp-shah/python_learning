no = int(input("Enter a number: "))
prime = True
for div in range(2 , no):
    if no % div == 0:
        prime = False
if prime:
    print("Prime")
else:
    print("Not prime")
