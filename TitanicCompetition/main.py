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

# Determining which parameters affect the probability of survival
print(train.columns)
# Pile 1
pile_1 = pd.Series(["PassengerId", "Age", "Fare"])
for param in pile_1:
    print(param + ": ", end="")
    print(train.loc[:, param].corr(train.Survived, method="pearson"))

for param in pile_1:
    print(train.loc[:, param].value_counts(bins=8, sort=False))

pile_2 = pd.Series(["Pclass", "Sex", "SibSp", "Parch", "Embarked"])
for param in pile_2:
    print(train.groupby(param).Survived.sum() / train.groupby(param).Survived.count())

for param in pile_2:
    print(train.groupby(param).Survived.count())

# for param in pile_1:
#     print(train.Survived.corr(train.loc(param), method="pearson"))
#
# passenger_test = pd.concat([train.PassengerId, train.Survived])
# passenger_corr = train.PassengerId.corr(train.Survived, method="pearson")
# print(passenger_corr)
#
# # Pclass
# # Finding probability of survival given a certain pclass
# prob_surv_pclass = train.groupby("Pclass").Survived.sum() / train.groupby("Pclass").Survived.count()
# print(prob_surv_pclass)
#
# # Relevant columns
# # Determining the probability of survival for each
# rel_col = train.columns.to_list()
# # The following columns do not have a significant effect on survival
# rel_col.remove("Name")
# rel_col.remove("PassengerId")
# rel_col.remove("Survived")
# rel_col.remove("Cabin")
#
# # Verifying that the remaining columns will affect survival
# for col in rel_col:
#     print(train.groupby(col).Survived.sum() / train.groupby(col).Survived.count())
