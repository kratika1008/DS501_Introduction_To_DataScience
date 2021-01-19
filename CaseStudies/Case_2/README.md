# Case Study 2: Tracking Recession using Financial Data (Python3)

## Goal:
Predict the likeliness of a recession using historical financial data (given no significant external impact).

## Key Indicators:
- Treasury Yield Curve
- Unemployment Data
- S&P 500 Graph

## Analysis Basis:
Recent Recessions occured in 1991, 2001, 2007-2008
Used the monthly data for various indicators through 1990 to 2006 and made a forecast for any recession after 2006

## Data Pre-processing:
- Used Quantopian data for the analysis
- Extracted US Unemployment rate using quandl 
- Got US Treasury Yield data and found three month to 10 years difference in the value
- Queried S&P 500 Index monthly average rate

## Prediction Analysis:
- Combined data related to various Indices
- Used Logistic Regression based on Scikit-learn library for the analysis
- Trained model on combined data till 2006
- Tested for all months after that

## Results:
Model predicted a recession of 6 months in 2007-2008 and 1 month of recession in 2020

## Requirements:
- matplotlib
- numpy
- pandas
- odo
- quantopian.interactive.data.quandl
- sklearn

