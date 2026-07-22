# Q12. Check Palindrome Number
# A number is palindrome if it reads the same backward and forward.

n = int(input("enter the number:"))

temp = abs(n)
if(n < 0):
    print("Not a palindrome number")
else:
    temp = n
    pal_num = 0
    while(n > 0):
        rem = n % 10
        pal_num = pal_num * 10 + rem
        n //= 10


    if(pal_num == temp):
        print("Palindrome number")
    else:
        print("Not a palindrome number")

