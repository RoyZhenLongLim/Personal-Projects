# * Useful Packages
# import numpy as np  # Linear Algebra
import pandas as pd  # data processing, CSV file, I/O

# ? train is the data of a subset of all passengers (more specifically 891, we
# ? to predict the fates of the remaining 418 passengers on board).
# train = pd.read_csv("Data/train.csv")
train = pd.read_csv("TitanicCompetition/Data/train.csv")

# ? test is the information of the remaining 418 passengers, there is no
# ? survived column
# test = pd.read_csv("Data/test.csv")
test = pd.read_csv("TitanicCompetition/Data/test.csv")

# * Determining which parameters affect the probability of survival
print(train.columns)
# * Pile 1
pile_1 = pd.Series(["PassengerId", "Age", "Fare"])
for param in pile_1:
    print(param + ": ", end="")
    print(train.loc[:, param].corr(train.Survived, method="pearson"))

# * Generate bins for data points that are unique but may have an impact on the survival

for param in ["PassengerId"]:
    bin = train.loc[:, param].value_counts(bins=6, sort=False).index
    for range in bin:
        survived = 0
        count = 0
        for person in train.loc[:, param]:
            if person in range:
                count = count + 1
            survived = survived + train.loc[train[param] == person]["Survived"]
        # print(param + ": Probability of surviving given they are in the range " + range + "is " + (survived/count))
        print(f"{param}:Probability of surviving given they are in the range {range} is {survived/count}")

train.loc[train["PassengerId"] == 600]["Survived"]

# * Determine the probability of survival of given a specified parameters
pile_2 = pd.Series(["Pclass", "Sex", "SibSp", "Parch", "Embarked"])
for param in pile_2:
    print(train.groupby(param).Survived.sum() / train.groupby(param).Survived.count())

# * Count how many people survived given a specified parameter
for param in pile_2:
    print(train.groupby(param).Survived.count())
