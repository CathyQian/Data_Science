## How to handle missing values?

Missing values are very common problems in machine learning. Below is a summary of common functions in Python and Pandas to process missing values.

#### Values considered missing: null, NaN, NaT or NA values:
- None: Pythonic missing data
- NaN: missing numerical value in Python
- NaT: missing values for datetime64[ns]

#### Detect missing values:
- pd.isna(df[column])
- df[column].notna()

#### Count missing values:
- df.isnull().sum()
- df.notnull().sum()

#### Remove rows with missing values:
- df.dropna(axis = 0, how = ‘any’)
- axis : 0 or ‘index’, 1 or ‘columns’
- how: ’any’ (if any NA values are present, drop that label), ‘all’ (if all values are NA, drop that label)

#### Filling missing values:
- df.fillna(value)

#### Fill missing values with mean column values:
- values = dataset.values
- imputer = Imputer()
- transformed_values = imputer.fit_transform(values)

#### Algorithms that can be made robust to missing data
- K-Nearest Neighbors that can ignore a column from a distance measure when a value is missing. Classification and regression trees
use the missing value as a unique and different value. However, the scikit-learn implementations of decision trees and K-Nearest
Neighbors are not robust to missing values.
- xgboost support missing values.



#### References:

1, https://pandas.pydata.org/pandas-docs/stable/missing_data.html

2, https://machinelearningmastery.com/handle-missing-data-python/

3, https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html


	
