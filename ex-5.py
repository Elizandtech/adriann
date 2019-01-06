# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

count =0
try:
    sumof = int(input('Enter a positive integer: '))
    if sumof <0:
        quit()
    while sumof >0:
        isdivisible = True
        sumof = sumof -1
        if sumof % 3!=0 and sumof % 5!=0:
            isdivisible = False
        elif sumof % 3==0 or sumof%5==0:
            count = sumof + count
    if isdivisible:
        print("The sum of the multiples of 3 and 5 within sumof is: ", count)
        
except:
    print("Didn't work.")


