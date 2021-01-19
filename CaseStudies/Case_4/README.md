# Case Study 4: Walmart Store Sales Prediction (Python3)

## Goal:
Accurately forecast weekly sales of Walmart

## Data Pre-processing:
- Used Walmart Sales dataset from Kaggle to evaluate weekly sale of the store
- Downloaded the data which includes details of various Walmart stores in different locations over different period of time
- Data includes various store features like Store Size, Store Type, Date, Holiday, Temperature, Discounts, Departments, etc
- Handled missing data
- Identified Public Holidays & Weekends using dates


## Analysis:
- Identified variation in Sales based on the Store Type
- Tried to look for any correlation between various features and removed redundant columns
- Run various Machine Learning models like Linear Regression, KNN Regressor, Decision Tree Regressor, Random Forest Regressor & XGBoost Regressor on the dataset to predict the sale


## Results:
- As expected, found that the sale is usually the highest around Black Friday and Christmas
- Random Forest & XGBoost Regressor provided the best result with small Root Mean Square error in predicting the Sale


## Requirements:
- matplotlib
- numpy
- pandas
- seaborn
- sklearn

