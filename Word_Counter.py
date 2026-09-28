text = input("Enter a sentence: ")

character_count = len(text)

words = text.split()
word_count = len(words)

uppercase_count = 0
lowercase_count = 0

for character in text:
    if character.isupper():
        uppercase_count += 1
    elif character.islower():
        lowercase_count += 1

print("Total Uppercase:", uppercase_count)
print("Total Lowercase:", lowercase_count)
print("Characters:", character_count)
print("Words:", word_count)



