try:
    maxnumber=int(input("Enter a positive integer greater than 1: "))
    if maxnumber<=1:
        print('No prime numbers to display.')
    for testnumber in range(2, maxnumber+1):
        isprime = True
        for div in range(2, testnumber):
            if testnumber % div== 0:
                isprime=False
                break
        if isprime:
            print(testnumber, end=" ")

except:
    print("Didn't work.")
            
                


