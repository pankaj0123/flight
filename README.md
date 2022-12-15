
# Flight Delay Prediction
When planning a trip, passengers should keep in mind that airlines do not guarantee their schedules. While airlines want to get passengers to their destinations on time, there are many things that can – and sometimes do – make it difficult for flights to arrive on time. Some problems, like bad weather, air traffic delays, and mechanical issues, are hard to predict and often beyond the airlines’ control. In this project we want predict the flight dealy.

## Understanding the Dataset
The dataset we are working on is a USA from 2013 and 2015. The dataset contains features 55 features like year, month, day.... The dataset contain both Numerical and Categorical dataset. This project we got different datasets of and we merged all the datasets and formed single dataset.

## Exploratory Data Analysis

In this Exploratory Data Analysis we started  basic exploring data whith shape of the dataset and info of dataset.


* Missing Values : Here we will check the percentage of nan values present in the in each features. There is a lot features contains nan values we have repleace this with meaningful which we will do in the Feature Engineering. 
* All The Numerical Variables:The dataset contains 39 Numerical Variables in that 16-Discrete variables and 21-Continuous features.   
* Outliers: We plot Box plot to see the outliers thers is more outliers we remove that in feature eangineering. 


## Feature Engineering
In feature engineering we treat the data that we seen in Exploratory Data Analysis
* Outlers:  In this process we used IQR method to remove outliers.
* Missing Values: In this proces we drop few columns containing 90% null values. After removing we used median method to fill Na values.

## Feature Selection
Feature selection we used Lasso and Selecteformmodel. In this setp we fit Independent features and got 2 fatures Flight and origin are Independent features.

## Model Building

### Logistic Regression
Logistic regression estimates the probability of an event occurring, such as delayed or not, based on a given dataset of independent variables. Since the outcome is a probability, the dependent variable is bounded between 0 and 1.

Model Accuracy = 55%

## Deployment
### Flask 
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[2] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

- The output will print where flight is delayed or not.
- The app runs on local host.
- To deplot it on the internet we have to deploy it on Heroku.

### Heroku
We deploy our Flask app to [https://flight-delay-model.herokuapp.com/].

We prepared the needed files to deploy our app sucessfully:
- Procfile: Contains run statements for app file.
- requirements.txt: contains the libraries must be downloaded by Heroku to run app file.
- app.py: contains the python code for a Flask web app.
- model.pkl: contains our Descion Tree Regressor model that built by modeling part.








