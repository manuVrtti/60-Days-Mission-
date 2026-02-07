from nltk.tokenize import sent_tokenize, word_tokenize

para_text = input("Enter a paragraph:\n")

print("\nProcessing text...\n")

sentence_tokens = sent_tokenize(para_text)

print("Sentence Tokens:")
print("----------------")

for each_sentence in sentence_tokens:
    current_sentence = each_sentence
    print(current_sentence)

print("\nWord Tokens:")
print("------------")

for each_sentence in sentence_tokens:
    word_list = word_tokenize(each_sentence)
    output_words = word_list
    print(output_words)

print("\nDone.")
