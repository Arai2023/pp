sentence = input()
word_list = sentence.split()
reversed_list = word_list[:: -1]
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)