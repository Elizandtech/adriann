# input a number, gives the sum of all numbers up to the given number.
x = 0
try:
    n = int(input('Enter a positive, non-zero integer: '))
    if n <= 0:
        quit()
    while n > 0:
        x = x + n
        n = n -1
    print (x)
except:
    print("Nobody likes a smartass.")


