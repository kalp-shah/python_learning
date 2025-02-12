a = float(input("Enter Basic Salary : " ))
if a > 10000:
        b = a * 25 / 100
        c = a * 15 / 100
        d = a * 20 / 100
elif a > 5000:
        b = a * 15 / 100
        c = a *  5 / 100
        d = a * 10 / 100        
else:
        b = a * 15 / 100
        c = a *  0 / 100
        d = a *  0 / 100
print ("Net Pay : ", a +b+c-d) 
input()
