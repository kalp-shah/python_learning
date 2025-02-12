start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))
if start < end:
    for no in range (start,end+1):
        print(no)
else:
    for no in range (end,start+1):        
        print(no)
