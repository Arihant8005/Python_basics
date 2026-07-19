#function that call itself
def show(n):
    if(n==0):           # base case
        return         #return from 0 to 1 to 2 to 3 to 4 to 5
    print(n)
    show(n-1)          # 5-1=4,4-1=3,3-1=2,2-1=1,1-1=0 then return

show(5)

#factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1) * n

print("Factorial : ", fact(5))