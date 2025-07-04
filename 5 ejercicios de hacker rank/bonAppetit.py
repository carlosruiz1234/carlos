
def bonAppetit (bill, k, b):
    # Write your code here
    total = sum (bill)
    total -= bill [k]
    if  b == total //2 : 
        return ("bon Appetit")
    else:
        return (b - total // 2)
    
print(bonAppetit([3,10,2,9,],0,7))