
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

## First Attempt 

To start off the first attempt, the first task is to clean the data.
- Since I don't know what data is actually important, I started by analysing whether a certain parameter would affect the probability of survival.
- Using this, we make some qualitative guess at what the machine learning model should return.
- To do this:
  - The data was sorted into three piles
    - Pile 1: Determine correlation between survival and parameter
      - This pile refers to Passenger_Id, Age, Fare.
      - This is because these tend to be unique, meaning instead of grouping them , it is better to see if there is a trend (e.g. whether survival increases with age)
    - Pile 2: Determine Probability of survival
      - This pile refers to Pclass, Sex, SibSp, Parch and Embarked
      - These piles generally only have a few unique options, meaning passenger can be easily grouped into them
    - Pile 3: Unused
      - Name, Cabin Number and Ticket are arbitrary 
      - There does not seem to be any pattern in the naming and are hence excluded
      - At the end of the analysis, additional test will be done including these parameters to ensure they do not contain any significant information
      - However, they will be excluded for the initial set of testing.

### Data Analysis Results

| Parameter    | Correlation Coefficient |
|--------------|-------------------------|
| Passenger_Id |                         |
| Age          |                         |
| Fare         |                         |
### Data Analysis

| Parameter    | Significance to Survival     | Extra Info |
|--------------|------------------------------|-----------| 
| PassengerId  | Low to None                  |           | 
