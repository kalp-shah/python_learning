no = int(input("Enter a number: "))
count = 0
for div in range(2 , no):
    if no % div == 0:
        count += 1
if count == 0:
    print("Prime")
else:
    print("Not prime")
