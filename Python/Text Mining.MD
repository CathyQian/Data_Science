# Below are summary notes of Applied Text Mining in Python by University of Michigan on Coursera.

## Week 1. Text cleaning 
Steps and templates used for text cleaning.
References:
- http://ieva.rocks/2016/08/07/cleaning-text-for-nlp/
- https://chrisalbon.com/python/cleaning_text.html

### 0. Read line from file
Read the line from list:

    for line in text:
        # do something with line

or read from file:

    with open('file.txt', 'r') as f:
        for line in f:
            # do something with line

### 1. Escaping HTML characters like &lt; &gt; &amp

    import HTMLParser
    html_parser = HTMLParser.HTMLParser()
    doc = html_parser.unescape(original_doc)

### 2. Decode data

    doc = original_doc.decode("utf8").encode(‘ascii’,’ignore’)
    line = line.decode('utf8')
    
### 3. Tokenize text

    from nltk.tokenize import word_tokenize
    raw_docs = [‘Today is a big day.’, ‘Dad is away.’, ‘A haircut cost me $25.’]
    tokenized_docs = [word_tokenize(doc) for doc in raw_docs]

### 4. Apostrophe Lookup: 

    APPOSTOPHES = {“'s" : " is", "'re" : " are", ...} ## Need a huge dictionary
    words = tweet.split()
    reformed = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]
    reformed = " ".join(reformed)

### 5. Remove symbols/numbers you don't need

    line = line.replace('+', ' ').replace('.', ' ').replace(',', ' ').replace(':', ' ')
    line = re.sub("(^|\W)\d+($|\W)", " ", line) # remove numbers
    
    # remove digits/numbers
    new_line = []
    for word in line.split():
        if not is_digit(word):
            new_line.append()
    line = " ".join(new_line)

    
### 6. Remove stopwords

    from nltk.corpus import stopwords   
    tokenized_docs_no_stopwords = []
    for doc in tokenized_docs_no_punctuation:
        new_term_vector = []
        for word in doc:
            if not word in stopwords.words('english'):
                new_term_vector.append(word)
        tokenized_docs_no_stopwords.append(new_term_vector)          
    print tokenized_docs_no_stopwords

### 7. Split Attached Words such as RainyDay, PlayingInTheCold 

    cleaned_doc = “ ”.join(re.findall(‘[A-Z][^A-Z]*’, original_doc))

### 8. Standardizing words such as looooooooove (to love)

    doc = ''.join(''.join(s)[:2] for _, s in itertools.groupby(doc))
    

********************************************************************************
********************************************************************************
********************************************************************************

### Mislaneous

    # word comparison functions
    s.startwith(t) # find string start with t in s iteratives
    s.endswith(t) # find string end with t
    t in s
    s.isupper()
    s.islower()
    s.istitle()
    s.isalpha()
    s.isdigit()
    s.isalnum()
    
    # string operations
    s.lower() # lowercase all letters
    s.upper() # uppercase all letters
    s.titlecase()
    s.split(t)
    s.splitlines() # solit the text by lines
    s.join(t)
    s.strip()
    s.rstrip() # remove the last character
    s.find(t) # find character t from the beginning of the string s, return position in s
    s.rfind(t) # find character t from the end of the string s, return position in s
    s.replace(u,v) # replace all character u with character v in s
    
    # file operations
    f = open(filename, mode)
    f.readline() # read in the first line of the text
    f.read()
    f.read(n)
    for line in f:
        doSomething(line)
    f.seek(n)
    f.write(message)
    f.close()
    f.closed
    
    
    # regular expression
    import re
    
    ^: start of a string
    $: end of a string
    [^abc]: matches a character that is not a, b or c
    [a-z]: matches one of the range of characters a, b, ...z
    
    \d: any digit, equivalent to [0-9]
    \D: any non-digit, equivalent to [^0-9]
    \w: alphanumeric character, equivalent to [a-zA-Z0-9_]
    \W: non-alphanumeric character, equivalent to [^a-zA-Z0-9_]
    \s: any whitespace, equivalent to [ \t\n\r\f\v]
    \S: any non-whitespace, equivalent to [^ \t\n\r\f\v]
    
    *: matches zero or more occurrances
    +: matches one or more occurrances
    ?: matches zero or one occurrances
    {n}: exactly n repetitions, n >= 0
    {n,}: at least n repetitions
    {,n}: at most n repetitions
    {m, n}: at least m and at most n repetitions
    
    re.findall(r'[aeiou]', text) # find all a, e, i, o, u in text
    
    encoding = 'utf-8'
