#By while loop

m = int(input("Enter the starting number: "))
n = int(input("Enter the last number: "))

i = m
while(i <= n):
    print(i ** 2, end = " ")
    i += 1
print()

#By for loop

for i in range(m , n +1):
    print(i ** 2, end = " ")