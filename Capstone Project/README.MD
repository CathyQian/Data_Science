### Introduction

An apartment rental listing includes content like text description, photos, number of bedrooms, price, etc and aims at attracting the most interest from potential renters. Therefore, both the apartment owners, potential renters and the website hosting the apartment rental listings are interested in figuring out how popular an apartment rental listing is. The goal of this project is 1) to predict whether an apartment rental listing is popular or not that popular 2) provide practical suggestions to the apartment owners on how to improve the popularity of apartments. Ideally these suggestions would be tested with randomized experimentation.

### Data
The data is from Kaggle Two-Sigma competition, which provides both training and testing data set for the apartment rental listings:
https://www.kaggle.com/c/two-sigma-connect-rental-listing-inquiries/data. 

The training dataset contains 49352 entries and 15 columns including interest_level. Here interest_level is the target variable and it’s 
defined as the number of inquiries a listing has in the duration that the listing was live on the site. The testing dataset contains 74659 entries and 14 columns (without interest_level).

All features are listed below:
- bathrooms: number of bathrooms
- bedrooms: number of bedrooms
- building_id: the id of the building
- created: date and time when the post is created
- description: description of the apartment
- display_address: display address of the apartment in the posting
- features: a list of features about this apartment
- latitude: latitude of the apartment
- listing_id: listing id of the apartment
- longitude: longitude of the apartment
- manager_id: id of the manager of the apartment
- photos: a list of photo links. You are welcome to download the pictures yourselves from renthop's site, but they are the same as imgs.zip. 
- price: in USD
- street_address: street address of the apartment
- interest_level: this is the target variable. It has 3 categories: 'high', 'medium', 'low'

### Methods
I’ll first reframe the problem as a three-class classification problem with interest_level as 'low' or 'medium' or 'high'. Then I’ll start with explanatory statistical analysis of the training data set, then clean the data and try out different feature engineers, followed by feeding engineered data into various machine learning algorithms, aiming to figure out the best combination of feature engineering and machine learning algorithms with the lowest log_loss via cross validation. Next, I’ll use optimized algorithm to predict the probability that each apartment listing falls into the three classes -- low, medium or high.

The deliverables include statistical analysis of the training dataset, IPython code for data wrangling, feature engineering and machine learning, as well as a summary report.
