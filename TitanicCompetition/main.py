# * Useful Packages
# import numpy as np  # Linear Algebra
import pandas as pd                                     # data processing, CSV file, I/O
from sklearn.ensemble import RandomForestRegressor      # used to generate the machine learning model
from sklearn.model_selection import train_test_split    # used to split data into training and validation data
from sklearn.metrics import mean_absolute_error         # used to determine accuracy of model

# ? train is the data of a subset of all passengers (more specifically 891, we
# ? to predict the fates of the remaining 418 passengers on board).
train = pd.read_csv("Data/train.csv")
# train = pd.read_csv("TitanicCompetition/Data/train.csv")

# ? test is the information of the remaining 418 passengers, there is no
# ? survived column
test = pd.read_csv("Data/test.csv")
# test = pd.read_csv("TitanicCompetition/Data/test.csv")

# * Determining which parameters affect the probability of survival
print(train.columns)

#%%

# * Pile 1
pile_1 = pd.Series(["PassengerId", "Age", "Fare"])

# Finding the correlation between survival and unique values

for param in pile_1:
    print(param + ": ", end="")
    print(train.loc[:, param].corr(train.Survived, method="pearson").round(2))

#%%

# * Determine the probability of survival of given a specified parameters
pile_2 = pd.Series(["Pclass", "Sex", "SibSp", "Parch", "Embarked"])

for param in pile_2:
    print(train.groupby(param).Survived.sum() / train.groupby(param).Survived.count())

# * Count how many people survived given a specified parameter
for param in pile_2:
    print(train.groupby(param).Survived.count())

#%%

RANDOM_CONSTANT = 1

parameters_used = ["PassengerId", "Age", "Fare", "Pclass", "Sex", "SibSp", "Parch", "Embarked"]
cleaned_data = train[parameters_used + ["Survived"]]
# Getting rid of the NAs
cleaned_data = cleaned_data.dropna(axis=0)
# Modify all the columns "Sex" and "Embarked" so that they represent integers (see documentation.md)
# Note the .loc method, first paramter specifies the row, second paramter specifies the column

# Establishing mapping between the two parameters
sex_map = {
    "male" : 0,
    "female" : 1
}

for key in sex_map.keys():
    cleaned_data.loc[cleaned_data.Sex == key, "Sex"] = sex_map[key]

embarked_map = {
    "C": 0,
    "Q": 1,
    "S": 2
}

for key in embarked_map.keys():
    cleaned_data.loc[cleaned_data.Embarked == key, "Embarked"] = embarked_map[key]

# Splitting the data into training and validation data
train_X, val_X, train_Y, val_Y = train_test_split(cleaned_data[parameters_used], cleaned_data.Survived, random_state=RANDOM_CONSTANT)

## Train the model
forest_model = RandomForestRegressor(random_state=RANDOM_CONSTANT)
forest_model.fit(train_X, train_Y)

# Verify how accurate the model is
pred = forest_model.predict(val_X)
print(mean_absolute_error(val_Y, pred))

#%%
