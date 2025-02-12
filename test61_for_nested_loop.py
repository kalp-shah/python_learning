for no in range (1,1000):
    sum = 0
    temp = no
    while no != 0:
        dig = no % 10
        no = no // 10
        sum = sum  + (dig*dig*dig)
    if sum == temp:
        print(temp)

