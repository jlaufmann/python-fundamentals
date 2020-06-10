'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

with open('words.txt', 'r') as fin:
	for line in fin.readlines():
		for word in (line.rstrip('\n')).split():
			if len(word) > 20:
				print(f"{word}")
