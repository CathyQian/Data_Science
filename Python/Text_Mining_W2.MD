# Below are summary notes of Applied Text Mining in Python by University of Michigan on Coursera.
## Week 2. Basic Natural Language Processing

Shallow NLP technique are used to extract key words or phrases (n-gram, n can be 2, 3, 4, ...) from texts. General steps involves: 

1) Convert the sentence to lowercase

2) Remove stopwords (these are common words found in a language. Words like for, very, and, of, are, etc, are common stop words)

3) Extract n-gram i.e., a contiguous sequence of n items from a given sequence of text (simply increasing n, model can be used to store more context)

4) Assign a syntactic label (noun, verb etc.)

5) Knowledge extraction from text through semantic/syntactic analysis approach i.e., try to retain words that hold higher weight in a sentence like Noun/Verb

All above can be implemented using NLTK packages in Python.

Ref: https://datascience.stackexchange.com/questions/5316/general-approach-to-extract-key-text-from-sentence-nlp


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
