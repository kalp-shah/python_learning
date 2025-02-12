item = input("Enter Item : ")
qty = int(input("Enter Qty : "))
rate = int(input("Enter Rate : "))
disc = 0
if item == "a" or item == "A":
    if qty > 50:
           disc = ((qty*rate) * 20 / 100)
    else:
           disc = ((qty*rate) * 10 / 100)
elif item == "b" or item == "B":
    if qty > 10:
           disc = ((qty*rate) * 15 / 100)
    else:
           disc = ((qty*rate) * 5 / 100)
else:
    print("calculate other number")
print("Amount   : ", qty*rate)
print("Discount : ", disc)
print("net Amt  : ",((qty*rate)-disc))
input()

