# Below are summary notes of Applied Text Mining in Python by University of Michigan on Coursera.
## Week 2. Basic Natural Language Processing
### NLTK (Natural Language Toolkit)

    import nltk
    
#### 0. Stem

    porter = nltk.PorterStemmer()
    [porter.stem(t) for t in wordslist]
  
#### 1. Lemmatization

    wnlemma = ntlk.WordNetLemmatizer()
    [wnlemma.lemmatize(t) for t in wordlist]
  
#### 2. Tokenization

    nltk.word_tokenize(wordlist) # tokenize words
    nltk.sent_tokenize(text) # tokenize sentence
  
#### 3. Part-of-speech (POS) Tagging

    ntlk.pos_tag(wordlist)

#### 4. Parsing sentence structure

    parser = nltk.ChartParser(grammer)
    trees = parser.parse_all(text) # return a tree structure indicating the sentence structure
  
#### 5. Words similarity (for words correction)

    nltk.jaccard_distance(set(nltk.ngrams(entry, n=3)), set(nltk.ngrams(candidate, n=3) # n = 3 means trigram
    nltk.edit_distance(entry, candidate)
