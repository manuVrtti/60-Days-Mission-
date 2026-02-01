import re
from collections import Counter

def split_words(sentence):
    return re.findall(r"\b[a-zA-Z]+\b", sentence.lower())

def count_freq(items):
    return Counter(items)

def filter_stopwords(words):
    common_words = {
        "a","an","the","and","or","but","if","because","so",
        "is","are","was","were","be","been","being",
        "in","on","at","to","for","of","with","by","from",
        "this","that","these","those",
        "it","its","they","them","their","you","your",
        "he","she","his","her","we","our","i","me","my"
    }
    return [w for w in words if w not in common_words]

input_text = input().strip()

word_list = split_words(input_text)
clean_words = filter_stopwords(word_list)
word_count = count_freq(clean_words)

print(word_list)
print(clean_words)
print(word_count)
