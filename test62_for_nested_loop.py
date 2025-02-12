count = 0
for no in range(1, 101):
    count = 0
    for div in range(2, no):
        if no % div == 0:
            count += 1
    if count == 0:
            print(no)
