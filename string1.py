# strings - sequence of characters

x = "hello"
# methods, loop
count = 0
vowel_count = []
for i in x:
    if i in ['a','e','i','o','u']:
        count = count + 1
        vowel_count.append(i)

print(f"the number of vowels in given string is : {count}")
print(vowel_count)


