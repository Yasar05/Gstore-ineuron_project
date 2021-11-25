**Overview/Problem statement:**

The 80/20 rule has proven true for many businesses–only a small percentage of customers produce most of the revenue. As such, marketing teams are challenged to make appropriate investments in promotional strategies.

We need to analyze a Google Merchandise Store (also known as GStore, where Google swag is sold) customer dataset to predict revenue per customer. Hopefully, the outcome will be more actionable operational changes and a better use of marketing budgets for those companies who choose to use data analysis on top of GA data.

# **End Goal:** To create an web application that can forecast revenue of the customers.
 
![image](https://user-images.githubusercontent.com/75694058/120646851-91ca6b80-c497-11eb-8779-fb8e8f0cddbe.png)

 
# Team Size:
The team consisted of:
- 1 Team Lead (Myself)
- 2 Dev-Ops engineers
- 2 QA engineers
- 1 UI developers
- 1 Data Scientists
- 5 Interns

# **Size of the data:**
Train: (903653, 55), 1.4GB
test: (804684, 53), 1.25GB
# **Data type of features:**
String 30, Integer 12, Decimal 6, Other 6

# Failure cases and solutions:
Major failure case happened in Model Building. the entire team was involved in it and the score we got was not more than 0.30. which was pretty bad.
We then did several iteration of preprocessing and feature engineering again and again. But things didnt work well. we didnt get any score more than that.
Finally a simple thing made increased the model performance. The mistake we were doing was spliting the data to train and test , by using train-test-split,
which was a random split.
So instead of doing a random split I thought why not we split the data by dates. The latest dates we can use as test data.
And there were minor changes/alteration that need to be done in feature engineering.
And this simple hack worked well. This scaled out model performance to 0.87, which was pretty good.
and then we hypertuned the model to get a better performance.

# **Challenges:**
Json data, Huge dataset, highly categorical data, takes time for model training and hyper parameter tuning:
# **Algorithms used:**
XGBoost, Random forest, LightGBM

# **HyperTuning techniques:**
RandomSearchCV, HyperOpt, Optuna

# **Deployment techniques:**
Flask, CI/CD pipeline, MLOps


create env

conda create -n wineq python=3.7 -y
activate env

conda activate wineq
created a req file

install the req

pip install -r requirements.txt
download the data from

#https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

git init
dvc init 
dvc add data_given/train.csv
git add .
git commit -m "first commit"
oneliner updates for readme

git add . && git commit -m "update Readme.md"
git remote add origin https://github.com/Priya1881/GA_MLOPS.git

git push origin main
tox command -

tox
for rebuilding -

tox -r 
pytest command

pytest -v
setup commands -

pip install -e . 
build your own package commands-

python setup.py sdist bdist_wheel

create an artifcats folder

mlflow server command -

mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./artifacts \
--host 0.0.0.0 -p 1234
