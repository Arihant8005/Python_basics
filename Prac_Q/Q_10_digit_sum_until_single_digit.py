# 10. Digit Sum Until Single Digit

# Keep adding the digits of a number until a single-digit result is obtained.
# Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2
# Concepts: loops, arithmetic, recursion (optional)

n=int(input("enter the number:"))
while(n>=10):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem
        n=n//10
    n=sum
print("Digit Sum Until Single Digit",sum)