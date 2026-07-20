# 3. Count Vowels in a String

# Input a string and count how many vowels (a, e, i, o, u) it has.
# Concepts: loops, string iteration, conditions

string=(input("enter string:"))
# print(string)
vowels = "aeiou"

count=0
for ch in string:
    if ch in vowels:
        count += 1
print("vowels:", count)