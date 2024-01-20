# Write a program to remove characters from a string starting from zero up to n and return a new string.

# pseudocode

# get user input for a string
word = input("Enter a word: ")

# get user input for the number of characters to remove
num = int(input("Enter the number of characters to remove: "))

# write a message about what the program does
print("Removing the first", num, "characters from the string.")

# remove the number of characters from the string
new_word = word[num:]

# print the new string
print(new_word)
