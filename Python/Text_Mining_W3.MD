### Week 3.

#### Using SKlearn's NaiveBayesClassifer

    from sklearn import naive_bayes
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    vect = TfidfVectorizer().fit(X_train)
    x = vect.transform(X_train)
    
    clf = naive_bayes.MultinomialNB()
    clf.fit(x, y_train)
    
    x_test = vect.transform(X_test)
    y_predict = clf.predict(x_test)


#### Using SKlearn's SVM

    from sklearn import svm
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    vect = TfidfVectorizer().fit(X_train)
    x = vect.transform(X_train)
    
    clf = svm.SVC()
    clf.fit(x, y_train)
    
    x_test = vect.transform(X_test)
    y_predict = clf.predict(x_test)
