'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.
'''

words = []
with open('words.txt', 'r') as fin:
	for line in fin.readlines():
		for word in (line.rstrip('\n')).split():
			words.append(word)			

# 1.
swlen = 99
for word in words:
	if len(word) <= swlen:
		if len(word) < swlen:
			swlen = len(word)
			shortest = [f"{word}"]
		else:
			shortest.append(word)
print(f"Shortest word(s): {shortest}")


# 2.
lwlen = 0
for word in words:
	if len(word) >= lwlen:
		if len(word) > lwlen:
			lwlen = len(word)
			longest = [f"{word}"]
		else:
			longest.append(word)
print(f"Longest word(s): {longest}")

# 3. 
print(f"Total words in file: {len(words)}")
