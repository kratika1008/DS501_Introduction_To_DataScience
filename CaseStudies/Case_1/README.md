# Case Study 1: Yelp Data Review Analysis

## Goal:
Analyze reviews of Businesses (Restaurants in our case) that have low rating (less than 2.5 out of 5) and highlight what people dislike about the place.

## Data Pre-processing:
- Downloaded Business and Review dataset from Yelp database
- Converted JSON files to CSV
- Identified that Restaurants make the largest dataset of all Reviews
- Extracted all reviews for one of the Demographic region (Phoenix, Arizona)
- Merged Business dataset with their Reviews

## Data Processing:
- Using Regex and NLTK library, cleansed all Review texts by removing punctuations and stop words
- Lemmatize words in text to their root word
- Identify Review Tags as Trigrams to help business identify areas of improvement

## Requirements:
- pandas
- matplotlib
- nltk
	- download punkt
	- download stopwords
- pil
- wordcloud


