for i in range(1 , 6):
    for c in range(1,6-i):
        print("  ", end="  ")        
    for c in range(1,i+1):
        print(c,end="   ")
    for c in range(i-1,0,-1):
        print(c, end="  ")        
    print()