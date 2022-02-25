sentence = """ Have free hours and love children? Drive kids to school, soccer practice and other activities."""

sentence = sentence.split()
bigrams = []

for i in range((len(sentence)-1)):
	bigrams.append((sentence[i], sentence[i+1]))
	# bigrams.append((i, i+1))
print(bigrams)