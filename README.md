**Overview:**

The 80/20 rule has proven true for many businesses–only a small percentage of customers produce most of the revenue. As such, marketing teams are challenged to make appropriate investments in promotional strategies.

We need to analyze a Google Merchandise Store (also known as GStore, where Google swag is sold) customer dataset to predict revenue per customer. Hopefully, the outcome will be more actionable operational changes and a better use of marketing budgets for those companies who choose to use data analysis on top of GA data.
**End Goal:** To create an web application that can forecast revenue of the customers.
**Single prediction:** 
https://gstore-pred.herokuapp.com/
 
**Batch prediction:**
https://revenueprediction.herokuapp.com/
 
**Size of the data:**
Train: (903653, 55), 1.4GB
test: (804684, 53), 1.25GB
**Data type of features:**
String 30, Integer 12, Decimal 6, Other 6
**Challenges:**
Json data, Huge dataset, highly categorical data, takes time for model training and hyper parameter tuning:
**Algorithms used:**
XGBoost, Random forest, LightGBM
**HyperTuning techniques:**
RandomSearchCV, HyperOpt, Optuna
**Deployment:**
Flask, MLOps, Heroku


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
