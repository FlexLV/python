
sentence = "Lists are ordered and Sets are not"
words = sentence.split()
unique_words = set(words)
word_lengths = {}

for word in unique_words:
    word_lengths[word] = len(word)

print(word_lengths)
