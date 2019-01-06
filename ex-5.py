# Modify the previous program (ex-4) such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15.

sums = 0 
try:
    sumof = int(input('Enter a positive integer: '))
    if sumof <0:                                                # Check that number is positive
        quit()
    while sumof >0:
        isdivisible = True                                      # Boolean value in variable
        sumof = sumof -1                                        # reduces input number by one to end the loop
        if sumof % 3!=0 and sumof % 5!=0:                       # Skip numbers not divisible by 3 or 5
            isdivisible = False
        elif sumof % 3==0 or sumof%5==0:
            sums = sumof + sums                                 # adds only numbers divisible by 3 or 5 to be summed
    if isdivisible:                                             
        print("The sum of the multiples of 3 and 5 within sumof is: ", sums)
        
except:
    print("Didn't work.")


