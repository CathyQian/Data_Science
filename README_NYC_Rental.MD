### Introduction

An apartment rental listing includes content like text description, photos, number of bedrooms, price, etc and aims at attracting the most 
interest from potential renters. Therefore, both the apartment owners, potential renters and the website hosting the apartment rental 
listings are interested in figuring out how popular an apartment rental listing is. The goal of this project is 1) to predict whether an 
apartment rental listing is popular or not that popular 2) provide practical suggestions to the apartment owners on how to improve the 
popularity of apartments. Ideally these suggestions would be tested with randomized experimentation.

### Data
The data is from Kaggle Two-Sigma competition, which provides both training and testing data set for the apartment rental listings:
https://www.kaggle.com/c/two-sigma-connect-rental-listing-inquiries/data. Properties of each apartment rental listing such as number of 
bathrooms, number of bedrooms, building_id, features, latitude, longitude, price, address and interest_level are listed in the dataset. 
The training dataset contains 49352 entries and 15 columns including interest_level. Here interest_level is the target variable and it’s 
defined as the number of inquiries a listing has in the duration that the listing was live on the site. The interest_level is expressed as 
‘low’, medium’, ‘high’ in the training set.

### Methods
I’ll first reframe the problem into a binary classification problem by combining apartments with ‘low’ or ‘medium’ interest_level as one 
category and ‘high’ as the other category. I’ll take 20% of the training data set out as testing data set and leave it untouched. Then I’ll
start with explanatory statistical analysis of the training data set, then clean the data and engineer the features, finally use machine 
learning methods to figure out the most important features associated with the interest_level. The next step is to feed these key features 
into different machine learning algorithms and use the training data set to train the machine learning algorithms and optimized it via 
cross validation. Next, I’ll use optimized algorithm to predict which category does each apartment in the testing data set fall into and 
calculate the prediction accuracy.

The deliverables include statistical analysis of the data set, SQL, R and python code for data wrangling, a paper shown in my Github account
and my personal blog.
