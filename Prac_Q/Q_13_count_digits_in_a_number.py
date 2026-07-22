# Q13. Count Digits in a Number
#  Count how many digits the number has.

n=int(input("enter the number:"))
count=0
for digits in str(abs(n)):
    count+=1
print("number of digits",count)
#OR
# n=int(input("enter the number:"))
# count=0
# while(n!=0):
#     count+=1
#     n=n//10
# print("number of digits",count)

    