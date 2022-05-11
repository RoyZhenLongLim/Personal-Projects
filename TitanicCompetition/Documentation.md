# Documentation

## Purpose

The purpose of this file is to help explain what the variables for easy
reference.

### Files and their meaning

| File Name             | Purpose                                                                                    |
|-----------------------|--------------------------------------------------------------------------------------------|
| gender_submission.csv | Example of a submission file if only female passengers survived.                           |
| train.csv             | The data used to create a model                                                            |
| test.csv              | The data of the remaining passenger, use the model to predict who survived and who doesn't |


### Data Variables 
| Variable     | Description                         | Details                                                                         |
|--------------|-------------------------------------|---------------------------------------------------------------------------------|
| Passenger Id |                                     |                                                                                 |
| Survived     | Whether they survived or not        | Survived = 1, Dead = 0                                                          |
| Pclass       | Passenger Class                     | Separated into 1st, 2nd and 3rd class                                           |
| Name         |                                     |                                                                                 |
| Sex          |                                     | Modified to Male = 0, Female = 1                                                |
| Age          |                                     |                                                                                 |
| SibSp        | Number of siblings/spouse onboard   |                                                                                 |
| Parch        | Number of parents/children on board |                                                                                 |
| Ticket       | Ticket Number                       |                                                                                 |
| Fare         | Cost of Ticket                      |                                                                                 |
| Cabin        | Cabin Number                        |                                                                                 |
| Embarked     | Port of Embarkation                 | C = Cherbourg, Q = Queenstown, S = Southampton, Modified to C = 0, Q = 1, S = 2 |
