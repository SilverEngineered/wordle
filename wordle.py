import pandas as pd

def yellow_check(y, word):
	for i in range(5):
		if len(y[i]) != 0:
			if any([j==word[i] for j in y[i]]) or not(all([j in word for j in y[i]])):
				return False
	return True
def filter_words(five_letter_words, g, y, b):
	possibilities = []
	for word in five_letter_words.keys():
		if yellow_check(y, word) and all([word[i] == g[i] for i in range(5) if g[i] != '1']) and all([b[i] not in word for i in range(len(b))]):
			possibilities.append(word)
	print(possibilities)

word_freq = pd.read_csv('unigram_freq.csv').set_index('word').to_dict()['count']
five_letter_words = {i: word_freq[i] for i in list(word_freq.keys()) if len(i) == 5}



g = '11111' # green letters (replace the 1 in the position with a letter if that letter is green)
y = [[],[],[],[],[]] # yellow letters (each empty list can be filled with characters to satisfy the yellow letters for the position in the word)
b = '' #black letters i.e letters that are not in the solution
filter_words(five_letter_words, g, y, b)
