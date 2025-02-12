start = float(input("enter start unit : "))
end = float(input("enter start unit : "))
units = end - start
calc = 0
if units <= 100:
    calc =  units * 7.00; 
elif units <= 200:
    calc =((100 * 7.00) + (units - 100) * 7.50); 
elif units <= 250:
    calc = ((100 * 7.00) + (100 * 7.50) + (units - 200) * 8.00); 
else:
    calc = ((100 * 7.00) + (100 * 7.50) + (50 * 8.00) + (units - 300) * 9.00); 
print(calc); 
