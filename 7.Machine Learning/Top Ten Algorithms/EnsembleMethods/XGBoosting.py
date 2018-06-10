# XGBoost
# notes:
# 1, learning rate or shrinkage should be set to 0.1 or lower, and smaller values will
# require the addition of more trees
# 2, the depth of trees should be configured in the range of 2-8 (no need to go deeper)
# 3, row sampling should be configured in the range of 30% to 80% of the training dataset
# (a) run the default configuration and review plots of the learning curves on the training and validation datasets
# (b) if the system is overlearning, decrease the learning rate and/or increase the number of trees
# (c) if the system is underlearning, speed the learning up to be more aggressive by increasing the learning rate or decreasing the number of trees
# (d) number of trees 100~ 1000, then tune the learning rate to find the best model.




import pandas as pd
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold


# read in x, y as numpy array
df = pd.read_csv('data.csv')
df = df.dropna(axis = 0, how = 'any')
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df['Embarkloc'] = df['Embarked'].map({'C': 1, 'Q': 2, 'S': 3})

y = df['Survived']
df = df.drop(['Survived', 'Sex', 'Embarked'], axis = 1)
x = df.values

# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = test_size, random_state = seed)
eval_set = [(X_test, y_test)]

# fit model no training data
model = XGBClassifier()
learning_rate = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.3]
param_grid = dict(learning_rate = learning_rate)
kfold = StratifiedKFold(y, n_folds = 10, shuffle = True, random_state = 7)
grid_search = GridSearchCV(model, param_grid, scoring = "log_loss", n_jobs = - 1, cv = kfold)
result = grid_search.fit(X_train, y_train)

# summarize results
print("BestL %f using %s" % (result.best_score_, result.best_params_))
means, stdevs = [], []
for params, mean_score, scores in result.grid_scores_:
    stdev = scores.std()
    means.append(mean_score)
    stdevs.append(stdev)
    print("%f (%f) with: %r" %(mean_score, stdev, params))    

# monitor performance and early termination
# use error evaluation to stop training once no further improvements have been made
# to the model.

# make predictions for test data
# fit model before making predictions
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%"%(accuracy*100.0))

print(model.feature_importances_)

plot_importance(model)
plt.show()

