# Finds all English words, the value of whose individual characters, if 
# mapped to a numbered list (1, 2, 3 ... 26), add up to exactly 100.
# Word list from SIL International Linguistics Department
# at http://www-01.sil.org/linguistics/wordlists/english/
# Inspired by the (in)famous HR gag of 'ATTITUDE' = 100%.
# Github @hktang

import time

def find_perfect_words(word_list):
	'''
	Take a list of words and return in a list all "perfect" words, i.e., 
	words adding up to exactly 100. 
	'''	
	chars = ['\r']
	hits = []
	start_time = time.time()
	for c in "abcdefghijklmnopqrstuvwxyz":
		chars.append(c)
	with open(word_list) as dic:
		for line in dic:
			word = line.strip("\n\r")
			score = 0
			for c in word:
				try:
					score += chars.index(c)
				except:
					score += 0
			if score == 100:
				hits.append(word)
	for hit in hits:
		print hit
	print "\nJob done.", str(len(hits)), "\"perfect\" words found in", \
	      time.time() - start_time, "seconds. \n"

find_perfect_words("vendor/words-en.txt")