'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

import string #allows for more advanced string functions

user_string = input("Please enter your string: ")
words_simple = user_string.split() #depending on punctuation marks in the string, this may not be very good

# stripping out punctuation marks:
words_raw = [word.strip(string.punctuation) for word in user_string.split()]

#converting all words to lower case so that 'cat', 'Cat' and CAT are treated as the same word:
words_lower = [word.lower() for word in words_raw]

print(f"Your string separated: {words_raw}")    # more for testing and troubleshooting
print(f"Unique words in string: {set(words_lower)}")    # useful user information

word_count = ['foo', 0]
for word in words_lower:
    if words_lower.count(word) > word_count[1]:
        word_count[0] = word
        word_count[1] = words_lower.count(word)

print(f"Word with most occurences: {word_count[0]}")
