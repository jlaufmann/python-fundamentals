'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

import string

user_string = input("Please enter your string: ")
words_simple = user_string.split() #not helpful

words_raw = [word.strip(string.punctuation) for word in user_string.split()]
words_lower = [word.lower() for word in words_raw]

print(f"Your string separated: {words_raw}")
print(f"Unique words in string: {set(words_lower)}")

word_count = ['foo', 0]
for word in words_lower:
    if words_lower.count(word) > word_count[1]:
        word_count[0] = word
        word_count[1] = words_lower.count(word)

print(f"Word with most occurences: {word_count[0]}")
