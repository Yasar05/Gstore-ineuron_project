# Overview:

The 80/20 rule has proven true for many businesses–only a small percentage of customers produce most of the revenue. As such, marketing teams are challenged to make appropriate investments in promotional strategies.
We need to analyze GStore customer dataset to predict revenue per customer. Hopefully, the outcome will be more actionable operational changes and a better use of marketing budgets for those companies who choose to use data analysis on top of GA data.

# End Goal: To create an web application that can forecast revenue of the customers.
# Single prediction: 
https://gstore-pred.herokuapp.com/
 
# Batch prediction:
https://revenueprediction.herokuapp.com/

# Size of the data:
# Train: (903653, 55), 1.4GB
# test: (804684, 53), 1.25GB
# Data type of features:
String 30, Integer 12, Decimal 6, Other 6
# Challenges:
Json data, Huge dataset, highly categorical data, takes time for model training and hyper parameter tuning:
# Algorithms used:
XGBoost, Random forest, LightGBM
# HyperTuning techniques:
RandomSearchCV, HyperOpt, Optuna
# Deployment:
Flask, MLOps, Heroku

