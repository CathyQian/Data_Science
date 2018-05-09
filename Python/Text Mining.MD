## Below are summary notes of Applied Text Mining in Python by University of Michigan on Coursera.

Week 1. Text cleaning 
Steps and templates used for text cleaning.
References:
http://ieva.rocks/2016/08/07/cleaning-text-for-nlp/
https://chrisalbon.com/python/cleaning_text.html

### tokenize text
from nltk.tokenize import word_tokenize
raw_docs = [‘Today is a big day.’, ‘Dad is away.’, ‘A haircut cost me $25.’]
tokenized_docs = [word_tokenize(doc) for doc in raw_docs]

# remove stopwords
from nltk.corpus import stopwords
tokenized_docs_no_stopwords = []
for doc in tokenized_docs_no_punctuation:
    new_term_vector = []
    for word in doc:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    tokenized_docs_no_stopwords.append(new_term_vector)
            
print tokenized_docs_no_stopwords
