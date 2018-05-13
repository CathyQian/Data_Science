### 1. Document Similarity

    import numpy as np
    import nltk
    from nltk.corpus import wordnet as wn
    import pandas as pd


    def convert_tag(tag):
        """Convert the tag given by nltk.pos_tag to the tag used by wordnet.synsets"""
    
        tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
        try:
            return tag_dict[tag[0]]
        except KeyError:
            return None


    def doc_to_synsets(doc):
        """
        Returns a list of synsets in document.
        """
        tokenized_doc = nltk.word_tokenize(doc)
        tags = nltk.pos_tag(tokenized_doc)
        s = []

        for i in range(len(tokenized_doc)):
            sy = wn.synsets(tokenized_doc[i], pos=convert_tag(tags[i][1]))
            if len(sy) > 0:
                s.append(sy[0])
        return s

    def similarity_score(s1, s2):
        """
        Calculate the normalized similarity score of s1 onto s2
        """
        max_simi_score = []
        for ss1 in s1:
            scores = [x for x in [ss1.path_similarity(ss2) for ss2 in s2] if x is not None]
            if scores:
                max_simi_score.append(max(scores))
            
        return sum(max_simi_score)/len(max_simi_score)


    def document_path_similarity(doc1, doc2):
        """Finds the symmetrical similarity between doc1 and doc2"""

        synsets1 = doc_to_synsets(doc1)
        synsets2 = doc_to_synsets(doc2)

        return (similarity_score(synsets1, synsets2) + similarity_score(synsets2, synsets1)) / 2
        
 ### 2. Topic Modeling
 
    import pickle
    import gensim
    from sklearn.feature_extraction.text import CountVectorizer

    # Load the list of documents
    with open('newsgroups', 'rb') as f:
        newsgroup_data = pickle.load(f)

    vect = CountVectorizer(min_df=20, max_df=0.2, stop_words='english', 
                       token_pattern='(?u)\\b\\w\\w\\w+\\b')
    # Fit and transform
    X = vect.fit_transform(newsgroup_data)

    # Convert sparse matrix to gensim corpus.
    corpus = gensim.matutils.Sparse2Corpus(X, documents_columns=False)

    # Mapping from word IDs to words (To be used in LdaModel's id2word parameter)
    id_map = dict((v, k) for k, v in vect.vocabulary_.items())

    ldamodel = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word = id_map, num_topics = 10, passes = 25, random_state = 34)
    # return topic list
    topic_list = ldamodel.show_topics(10)
