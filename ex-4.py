## Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.

sums = 0
try:
    somenum = int(input("Enter a positive integer: "))
    if somenum < 0:                             # check that input number is positive
        quit()
    while somenum > 0:
        sums = sums + somenum                   # adds numbers to be summed
        somenum = somenum - 1                   # reduces input number by one to end the loop
    print("Sum is: ", sums)
except:
    print("Didn't work.")

