### What machine learning algorithm to use in practical applications?

It depends. Below are questions to consider when deciding which algorithms to use:
-	Is it classification or regression problem?
-	How much data do you have & is it continuous?
-	Is data class linear?
-	Which one has priority: accuracy or speed?

### 1. General Guidelines
#### Number of features
For certain types of data, the number of features can be very large compared to the number of data points. This is often the case with genetics or textual data. The large number of features can bog down some learning algorithms (i.e., support vector machine), making training time unfeasibly long.

#### Linearity
Lots of machine learning algorithms make use of linearity. Linear classification algorithms assume that classes can be separated by a straight line (or its higher-dimensional analog), for example, logistic regression. Linear regression algorithms assume that data trends follow a straight line. These assumptions aren't bad for some problems, but on others they bring accuracy down. Despite their dangers, linear algorithms are very popular as a first line of attack. They tend to be algorithmically simple and fast to train.

#### Accuracy VS Speed
Getting the most accurate answer possible isn't always necessary. Sometimes an approximation is adequate, depending on what you want to use it for. If that's the case, you may be able to cut your processing time dramatically by sticking with more approximate methods. 

### 2. Comparison of top machine learning algorithms

-------------  linear regression, logistic regression, Naïve Bayes, decision trees, random forests/XGBoost, KNN, Kmeans, PCA, SVM, NN  --------

- linear regression: for linear fitting, may be overly simple for some problems
- logistic regression: good for binary and multiclass classification. Gives linear class boundary, so when you use it, make sure a linear approximation is something you can live with.
- decision trees, random forests, XGBoost: regression, two-class, and multiclass ( they all do the same thing—subdivide the feature space into regions with mostly the same label), may be slow if the trees have too many branches.
- neural network: multiclass, two-class, regression; can handle complex nonlinear relationships, takes a long time to train, have more parameters than most algorithms
- support vector machine: two-class, can handle complex nonlinear relationships, run fast, among the best with limited data.
- Naïve Bayes: two-class, linear regression; mostly used at text classification and multi-class, avoid overfitting, have very few parameters , quick for large data sets, good when CPU and memory resources are a limiting factor, but based on the assumption that the features are independent.
- PCA: dimension reduction, anomaly detection
- K-means: clustering
- KNN: classification, simple, often effective but slow and requires lots of memory.

### 3. Algorithms to use for different types of problems
- Classification (supervised ML) (two-class or multi-class):
Naïve Bayes, logistic regression, SVM, decision trees, random forests, XGBoost, neural network, KNN

- Regression (supervised ML): linear regression, KNN, decision trees, random forests, XGBoost, Neural network
- Clustering (unsupervised ML): KMeans
- Dimensionality reduction: PCA

Scikit-learn machine learning map also gives intuitive guidelines on what algorithms to use. 
Ref: http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html



### References:
https://docs.microsoft.com/en-us/azure/machine-learning/studio/algorithm-choice
https://www.datasciencecentral.com/profiles/blogs/want-to-know-how-to-choose-machine-learning-algorithm

