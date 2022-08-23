
# Intro

This is a folder dedicated to showcasing my data analysis and machine learning
capabilities which are demonstrated using Kaggle's Titanic Competition where,
given a set of data, you must predict who will survive the historical event
(pretty cool aye!). I will document the struggles I experience and how I
overcame them.  
I have also included code to demonstrate what type of coder I am.  
Please see documentation for a more in-depth explanation of the data used.

# Struggles

## Knowledge

Prior to this competition, I had some experience in data analysis, primarily
from the actuarial science part of my degree since I need to do R coding.
However, for this competition, the language used Python and in particular,
Pandas, which is a package specifically for data analysis. Since I wasn't
familiar with the concepts, I was forced do a brief course on it on Kaggle. In
addition, the competition required you to submit a prediction based on what data
analysis, which required machine learning knowledge, which I had no experience
with, meaning I had to do another mini-machine learning course in my own time on
Kaggle.

## Data Cleaning & Analysis

To start off the first attempt, the first task is to clean the data.
- Since I don't know what data is actually important, I started by analysing whether a certain parameter would 
  affect the probability of survival.
- Using this, we make some qualitative guess at what the machine learning model should return.
- To do this:
  - The data was sorted into three piles
    - Pile 1: Determine correlation between survival and parameter **OR** any other special treatment
      - This pile refers to PassengerId, Age, Fare.
      - This is because these tend to be unique, meaning instead of grouping them, it is better to see if there is 
        a trend (e.g. whether survival increases with age) 
      - The data will also be grouped into a few different columns to see if a specific range of values (e.g. age 
        between 0 - 20) would provide a higher probability of survival
    - Pile 2: Determine Probability of survival
      - This pile refers to Pclass, Sex, SibSp, Parch and Embarked
      - These piles generally only have a few unique options, meaning passenger can be easily grouped into them
    - Pile 3: Unused
      - Name, Cabin Number and Ticket are arbitrary 
      - There does not seem to be any pattern in the naming and are hence excluded
      - At the end of the analysis, additional test will be done including these parameters to ensure they do not 
        contain any significant information 
      - However, they will be excluded for the initial set of testing.

### Data Analysis Results

The data has been rounded to two decimal points to help with presentation.

#### Pile 1 

| Parameter    | Correlation Coefficient |
|--------------|-------------------------|
| Passenger_Id | -0.01                   |
| Age          | -0.08                   |
| Fare         | 0.26                    |

#### Pile 2 

To understand the following table, it is important to note that the probability of survival is:
```markdown
Probability of Survival = Pr(Alive | Parameter = Specified)
```
For example,  the probability of PClass, 1st means the probability that a person in the 1st Passenger Class will 
survive is 0.63 or 63%.


| Parameter | Probability of Survival                                      | Additional Information                                                                                       | 
|-----------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| PClass    | 1st = 0.63, 2nd = 0.47, 3rd = 0.24                           | Number of people in Pclass are: 1 = 216, 2 = 184, 3 = 491                                                    |
| Sex       | M = 0.19, F = 0.74                                           | Number of: M = 577, F = 314                                                                                  |
| SibSp     | 0 = 0.35, 1 = 0.54, 2 = 0.46, 3 = 0.25                       | Number of people with x siblings/spouses are: 0 = 608, 1 = 209, 2 = 28, 3 = 16, 4 = 18, 5 = 5, 8 = 7         |  
| Parch     | 0 = 0.34, 1 = 0.55, 2 = 0.5, 3 = 0.60, 4 = 0, 5 = 0.2, 6 = 0 | Number of people with x number of parents/children are: 0 = 678, 1 = 118, 2 = 80, 3 = 5, 4 = 4, 5 = 5, 6 = 1 |

### Data Analysis

#### Pile 1 Analysis 

Looking at the result, it seems that both Passenger Id and Age do not have a significant impact on whether someone 
will live or die.  
However, it seems like the fare does have a weak-moderate correlation to survival.
- This makes sense as those who paid more in terms of fare may have been given better safety measures or perhaps 
  given cabins that are near the top of the Titanic for a better view and hence have a greater probability of 
  getting to safety when the Titanic began to sink

#### Pile 2

Pclass seems to be a significant factor in predicting the survival of people. Since Pclass is tied to the fare, the 
argument made on why fare would affect survival is also relevant here.  

Sex is also a major factor in determine survival. Despite there being less women relative to men, the probability of 
survival is much higher, which makes sense given that it is common knowledge that during the evacuation, women and 
children were prioritised when it comes to get a spot on the lifeboats.

It would also seems that the number of sibling, spouse, parent or children have a positive impact on survival as the 
probability of survival rose with the number of family members (note I am ignoring the data points where people have 
more than 3 family members on board as they are a minority and may skew the data).

### Afterthoughts

Once I started to do some data analysis, I realised the approach for the unique values wasn't ideal since age is 
likely to create a difference in survival rate since children were more likely to be evacuated, no matter the
gender. It would be more appropriate to group data in pile 1 before I start. Unforunately, I couldn't get this to work
so this will be put on a to do list for later in the project.


## Applying Machine Learning

### Basic Procedure

**TLDR**  
Using Random Forest Regressors (multiple decisions trees) and using mean absolute error as a mean of accuracy.  
**End of TLDR**  

The machine learning package used here is sklearn.ensemble.

- This package provides a random forest regressor, which will create multiple decision trees
- Although this package is considered to be slow, it should get the work done.

The random forest regressor has a number of parameters can we tweak to suit our use. These include:

- n_estimators: number of trees
- max_features: max number of features considered for splitting a node 
- max_depth: max number of levels in each decision tree
- min_sample_split: min number of data points placed in a node before the node splits
- min_samples_leaf: min number of data points allowed in a leaf node
- bootstrap: method for sampling data points

Credit to
this [article](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)
for recommendations on hyperparameter tuning 

- Method in this article will be used starting from attempt 3

The parameters we will be using to predict survival:

- Passenger Id
- Age
- Fare
- Passenger Class
- Sex
- Number of sibling and spouse
- Number of parents and children
- Port of embarkation

The data will be split up into two piles (different from the analysis stage) with one being the validation data and one
being data used to train the model on.

For the purpose of consistency, we will limit the amount of randomness present in the model to monitor its progress.
- the parameter associated with randomness in the sklearn package will be set to some constant
  - this parameter is known as `randomstate`

To measure how accurate the model is, we will use mean absolute error (MAE)  


### Issues that popped up

How the package seemed to work was that it converted all parameters into floats.

- This works fine for most parameters since they were either integers or floats already.
- This does not work with the parameters that are strings, for example, the parameter "Sex" had two different strings (
  male and female) as its values
- To get around this issue, we had to modify the data such that **ALL** data fed into the machine learning package was
  either a float or an integer

### Result

#### Attempt 1

###### Results
The data will be shown to 4 significant figures to better evaluate the difference.

- MAE = 0.2627
- Not the best but it's a start

##### Adjustment made
- Will vary the leaf node to see how it affects the accuracy of the model

#### Attempt 2

##### Results
| Max Number of Leaf Nodes | MAE    |
|--------------------------|--------|
| 5                        | 0.2755 |
| 50                       | 0.2568 |
| 500                      | 0.2635 |
| 5000                     | 0.2635 |
| 50000                    | 0.2635 |

As we reach higher leaf number of leafs nodes, we can see that past a certain point (around 500) that the extra leaf
nodes do not have any influence on the MAE.  
It would be ideal for the leaf node to be 50 - 500.

- Set to 50 for the time being as it is the best one we have

##### Adjustments made

Although we tried just changing the leaf nodes, in reality there are a dozen of settings we can change.  
This calls for more advanced parameter setting.

We will be using
the [documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) from
the sklearn page to tune the random forest regressor alongside Randomized Search CV (also from sklearn) which will pick
parameters for each iteration.

#### Attempt 3 
