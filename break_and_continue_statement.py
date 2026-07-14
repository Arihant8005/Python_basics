i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print()

i=1
while i<=5:
    if(i==3):
        i+=1                
        continue
    print(i)
    i+=1
print()
    
i=1
while i<=10:
    if(i%2!=0):
        i+=1               # printing only even numbers using continue statement
        continue
    print(i)
    i+=1