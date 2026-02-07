import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# initialize stemmer and lemmatizer
ps = PorterStemmer()
wnl = WordNetLemmatizer()

# input reviews
review_list = [
    "The product is running very smoothly and works perfectly.",
    "I was disappointed with the quality of the product.",
    "The delivery was fast and the packaging was excellent."
]

print("Text Processing Started...\n")

for single_review in review_list:

    # convert to lowercase
    lowered_text = single_review.lower()

    # remove punctuation
    cleaned_text = lowered_text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # tokenize words
    token_words = word_tokenize(cleaned_text)

    # apply stemming
    stem_result = []
    for w in token_words:
        stem_word = ps.stem(w)
        stem_result.append(stem_word)

    # apply lemmatization
    lemma_result = []
    for w in token_words:
        lemma_word = wnl.lemmatize(w)
        lemma_result.append(lemma_word)

    print("Original Review:")
    print(single_review)

    print("Stemmed Output:")
    print(stem_result)

    print("Lemmatized Output:")
    print(lemma_result)

    print("-" * 40)

print("\nProcessing Completed.")
