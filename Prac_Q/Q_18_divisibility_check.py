#Find Numbers That Are Divisible by Both 3 and 5 (1 to 100)

list =[]
for i in range(1 , 100):
    if(i % 3 == 0 and i % 5 == 0):
        list.append(i)

print(list)