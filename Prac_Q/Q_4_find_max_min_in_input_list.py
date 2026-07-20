# 4. Find the Maximum and minimum value in an input list

# Take n numbers from the user and find the maximum and minimum manually.
# Concepts: comparison logic, iteration

num=[int(x) for x in input("enter numbers: ").split()]

# print(max(num))          # we dont have to do this

max = min = num[0]

for val in num:
    if(val > max):
        max = val
    elif(val < min):
        min = val

print("maximum value is: ", max)
print("minimun value is: ", min)
