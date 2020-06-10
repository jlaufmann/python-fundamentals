'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

words = []
with open('words.txt', 'r') as fin:
	for line in fin.readlines():
		for word in (line.rstrip('\n')).split():
			words.append(word)

# 1. assuming it is just the word order to be reversed, and not the letters in each word:
with open('reverse.txt', 'w') as fout:
	for word in words[::-1]:
		fout.write(f"{word}\n")

# 2. if the letters in the words are to be reversed too:
with open('reverse2.txt', 'w') as fout:
	for word in words[::-1]:
		fout.write(f"{word[::-1]}\n")
