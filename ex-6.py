## Write a program that asks the user for a number n and gives them the option of computing the sum and computin the product of 1,...n. 
try:
    number = int(input("Enter a positive integer: "))
    if number <0:
        quit() 
    choice = input("Do you want the sums or products (enter sum or product)?: ")
    if choice != 'sum' and choice !='product':
        quit()
    if choice =='sum':
        count =0
        for num in range(1, number+1):
            count = num + count
        print(count)
    if choice=='product':
        product = 1
        for multiplier in range(1, number+1): 
            product = multiplier*product
        print(product)

except:
    print("Oh that ain't right.")

#def 

