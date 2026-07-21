# 9. List Comprehension Challenge

# Create a list of all (x, y) coordinates where x + y is not equal to 4, for x, y in range 0–3.
# Concepts: nested loops, logical filtering

x = int(input("Enter x: "))
y = int(input("Enter y: "))              #it a genearl way to solve this type of Q.
n = int(input("Enter n: "))

result = [[i, j] for i in range(x+1)
                      for j in range(y+1)
                      if(i + j!= n)]

print(result)
