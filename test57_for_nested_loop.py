for i in range(1 , 6):
    for c in range(1,6-i):
        print("  ", end="  ")        
    for c in range(i,2*i):
        print(c,end="   ")
    for c in range(2*i-2,i-1,-1):
        print(c, end="  ")        
    print()    
