for i in range(1 , 6):
    for c in range(1,6-i):
        print("  ", end="  ")        
    for c in range(1,2*i):
        print("*",end="   ")  
    print()    
