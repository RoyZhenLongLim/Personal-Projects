
# * Useful Packages
import numpy as np # Linear Algebra
import pandas as pd # data processing, CSV file, I/O

# * Importing data and what they do
# ? The data contains
# ? "PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch",
# ? "Ticket", "Fare", "Cabin", "Embarked"

# ? train is the data of a subset of all passengers (more specifically 891, we
# ? to predict the fates of the remaining 418 passengers on board).
# train = pd.read_csv("Data/train.csv")
train = pd.read_csv("TitanicCompetition/Data/train.csv")
print(train.head)

# ? test is the information of the remaining 418 passengers, there is no
# ? survived column
# test = pd.read_csv("Data/test.csv")
test = pd.read_csv("TitanicCompetition/Data/test.csv")


