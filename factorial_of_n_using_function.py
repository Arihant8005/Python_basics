def cal_fact(n):
    i=1
    fact=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)

cal_fact(5)
cal_fact(4)

# #OR by using for loop
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

factorial(6)
factorial(8)