# * Useful Packages
import numpy as np
import pandas as pd  # data processing, CSV file, I/O
from sklearn.ensemble import RandomForestRegressor  # used to generate the machine learning model
from sklearn.metrics import mean_absolute_error  # used to determine accuracy of model
from sklearn.model_selection import train_test_split  # used to split data into training and validation data
from sklearn.model_selection import RandomizedSearchCV  # used to allow for randomized parameters

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

# %%

# * Pile 1
pile_1 = pd.Series(["PassengerId", "Age", "Fare"])

# Finding the correlation between survival and unique values

for param in pile_1:
    print(param + ": ", end="")
    print(train.loc[:, param].corr(train.Survived, method="pearson").round(2))

# TODO Group data before analysis

# %%

# * Determine the probability of survival of given a specified parameters
pile_2 = pd.Series(["Pclass", "Sex", "SibSp", "Parch", "Embarked"])

for param in pile_2:
    print(train.groupby(param).Survived.sum() / train.groupby(param).Survived.count())

# * Count how many people survived given a specified parameter
for param in pile_2:
    print(train.groupby(param).Survived.count())

# %%

RANDOM_CONSTANT = 1

parameters_used = ["PassengerId", "Age", "Fare", "Pclass", "Sex", "SibSp", "Parch", "Embarked"]
cleaned_data = train[parameters_used + ["Survived"]]
# Getting rid of the NAs
cleaned_data = cleaned_data.dropna(axis=0)
# Modify all the columns "Sex" and "Embarked" so that they represent integers (see documentation.md)
# Note the .loc method, first paramter specifies the row, second paramter specifies the column

# Establishing mapping between the two parameters
sex_map = {
    "male": 0,
    "female": 1
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

# %%

# Attempt 1

# Splitting the data into training and validation data
train_X, val_X, train_Y, val_Y = train_test_split(cleaned_data[parameters_used], cleaned_data.Survived,
                                                  random_state=RANDOM_CONSTANT)

## Train the model
forest_model = RandomForestRegressor(random_state=RANDOM_CONSTANT)
forest_model.fit(train_X, train_Y)

# Verify how accurate the model is
pred = forest_model.predict(val_X)
mae_v1 = mean_absolute_error(val_Y, pred)
print(f"The MAE for attempt 1 is {mae_v1}")


# %%

# Attempt 2
# Since we are doing essentially the same thing, I will make a function that automatically computes MAE
def get_mae(max_leaf_node, train_X, val_X, train_Y, val_Y):
    model = RandomForestRegressor(max_leaf_nodes=max_leaf_node, random_state=RANDOM_CONSTANT)
    model.fit(train_X, train_Y)
    pred = model.predict(val_X)
    return mean_absolute_error(val_Y, pred)


# Vary the leaf node and verify the difference in MAE
leaf_node_sizes = [5, 50, 500, 5000, 50000]
for size in leaf_node_sizes:
    mae = get_mae(size, train_X, val_X, train_Y, val_Y)
    print(f"Max leaf nodes: {size} \t\t Mean Absolute Error {mae}")

mae_v2 = get_mae(50, train_X, val_X, train_Y, val_Y)
print(f"The MAE for attempt 2 is {mae_v2}, this is an improvement of {mae_v1 - mae_v2}")

# %%

# Attempt 3
# Number of trees used is between 200 - 2000, the following will generate 10 equally spaced values
n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
# Number of features ot consider at every split/node
max_features = ["auto", "sqrt", "log2"]
# Max level in tree, create 10 to 110 equally spaced levels
max_depth = [int(x) for x in np.linspace(10, 110, num=10)]
max_depth.append(None)
# Minimum number of samples required for a split
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree, if false, use the whole data set to build each tree
boostrap = [True, False]

random_grid = {
    "n_estimators": n_estimators,
    "max_features": max_features,
    "max_depth": max_depth,
    "min_samples_leaf": min_samples_leaf,
    "min_samples_split": min_samples_split,
    "bootstrap": boostrap
}

rf = RandomForestRegressor(random_state=RANDOM_CONSTANT)

rf_random = RandomizedSearchCV(
    estimator=rf,
    param_distributions=random_grid,
    n_iter=100,
    cv=3,
    verbose=2,
    random_state=RANDOM_CONSTANT,
    n_jobs=-1
)
rf_random.fit(
    train_X,
    train_Y
)

pred = rf.predict(val_X)
print(mean_absolute_error(val_Y, pred))
# rf_random.best_params_

# pred = rf_random.best_estimator_.predict(val_X)
# mae_v3 = mean_absolute_error(pred, val_Y)
#%%


