# Write a program that prints a multiplication table up to 12.

try:
    table = int(input("Enter table type(i.e. 12, 15, etc.) up to 37: "))
    for i in range(0,table+1):
        print("%4d"%(i), end=" ")
        for n in range(1, table+1):
            print("\n")
            m=n*i
            print("%4d"%(m), end=" ")
        print("\n")
except:
    print("Didn't work.")

