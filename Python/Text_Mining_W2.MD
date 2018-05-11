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
    from nltk.corpus import words

    correct_spellings = words.words()
    nltk.jaccard_distance(set(nltk.ngrams(entry, n=3)), set(nltk.ngrams(candidate, n=3) # n = 3 means trigram
    nltk.edit_distance(entry, candidate)
    
    # find correct spellings for entries
    def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
    
    results = []
    for entry in entries:
        candidates = [w for w in correct_spellings if w[0] == entry[0]]
        results.append(min(candidates, key=
                           lambda candidate:nltk.edit_distance(entry, candidate)))
    
    return results
