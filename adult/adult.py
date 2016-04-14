import pandas

adult = pandas.read_csv("Data/data.csv")

print adult.describe()



#mapping functions
def map_workclass(x):
    if x == "Without-pay" or x == "Never-worked":
        return int(0)
    elif x == "Private":
        return int(1)
    elif "-gov" in x:
        return int(3)
    else:
        return int(4)

def map_education(x):
    grad = ["HS-grad", "Some-college"]
    postgrad = ["Bachelors"]
    if "th" in x or x == "Preeschool":
        return int(0)
    elif x in grad:
        return int(1)
    elif "Assoc" in x:
        return int(3)
    elif x in postgrad:
        return int(2)
    else:
        return int(4)

def map_marital(x):
    not_married = ["Married-spouse-absent", "Divorced", "Separated",
                   "Never-married", "Widowed"]
    if x in not_married:
        return int(0)
    else:
        return int(1)

def map_race(x):
    if x == "White":
        return int(0)
    else:
        return int(1)

def map_country(x):
    if x == "United-States":
        return int(0)
    else:
        return int(1)
    
def map_occupation(x):
    admin = ["Adm-clerical"]
    military = ["Armed-Forces"]
    blue_collar = ["Craft-repair", "Farming-fishing", "Handlers-cleaners",
                   "Machine-op-inspct", "Transport-moving"]
    service = ["Other-service", "Priv-house-serv", "Protective-serv"]
    professional = ["Prof-specialty"]
    sales = ["Sales"]
    if x in military:
        return int(1)
    elif x in blue_collar:
        return int(2)
    elif x in service:
        return int(3)
    elif x in professional:
        return int(4)
    elif x in sales:
        return int(5)
    else:
        return int(6)


def map_age(x):
    if x < 30:
        return int(0)
    else:
        return int(1)


#Converting non-numeric columns
#workclass
adult.workclass = adult.workclass.map(map_workclass)

#education
adult.education = adult.education.map(map_education)

#marital-status
adult["marital-status"] = adult["marital-status"].map(map_marital)

#occupation
adult.occupation = adult.occupation.map(map_occupation)

#race
adult.race = adult.race.map(map_race)

#sex
adult.loc[adult["sex"] == "Male", "sex"] = 0
adult.loc[adult["sex"] == "Female", "sex"] = 1

#native-country
adult["native-country"] = adult["native-country"].map(map_country)


#Rest of non-numeric columns have been ignored
#simplifying age and capital hours
adult.age = adult.age.map(map_age)
adult["capital"] = adult["capital-gain"] + adult["capital-loss"]

adult.loc[adult["income"] == "<=50K", "income"] = 0
adult.loc[adult["income"] == ">50K", "income"] = 1

#On to machine learning
#We'll use linear regression and cross validation
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold

#The columns we'll use to predict the target
predictors = ["age", "workclass", "marital-status", "occupation", "race", "sex", "education-num",
              "native-country","capital", "hours-per-week", "education"]

#Initialize algorithm
alg = LinearRegression()

#Generate cross validation
kf = KFold(adult.shape[0], n_folds=3, random_state=1)

predictions = []
for train, test in kf:
    #Predictors we are using to train the algorithm
    train_predictors = adult[predictors].iloc[train]
    #Target for training
    train_target = adult["income"].iloc[train]
    #Training algorithm
    alg.fit(train_predictors, train_target)

    #Making predictions on the test fold
    test_predictions = alg.predict(adult[predictors].iloc[test,:])
    predictions.append(test_predictions)
    
#Logistic regression to clean up and map predictions to (1, 0)
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
alg = LogisticRegression()
scores = cross_validation.cross_val_score(alg, adult[predictors], [x for x in adult["income"]], cv = 3)

print "Predictions done with accuracy of: ", scores.mean(), "\n"

adult_test = pandas.read_csv("Data/test.csv")

#Processing the test set
adult_test.workclass = adult_test.workclass.map(map_workclass)

#education
adult_test.education = adult_test.education.map(map_education)

#marital-status
adult_test["marital-status"] = adult_test["marital-status"].map(map_marital)

#occupation
adult_test.occupation = adult_test.occupation.map(map_occupation)

#race
adult_test.race = adult_test.race.map(map_race)

#sex
adult_test.loc[adult_test["sex"] == "Male", "sex"] = 0
adult_test.loc[adult_test["sex"] == "Female", "sex"] = 1

#native-country
adult_test["native-country"] = adult_test["native-country"].map(map_country)

adult_test.loc[adult["income"] == "<=50K", "income"] = 0
adult_test.loc[adult["income"] == ">50K", "income"] = 1

#simplifying age and capital gains
adult_test.age = adult_test.age.map(map_age)
adult_test["capital"] = adult_test["capital-gain"] + adult_test["capital-loss"]

#Generating submission file
print "Generating submission file..."
alg = LogisticRegression(random_state=1)
alg.fit(adult[predictors], [x for x in adult["income"]])

predictions = alg.predict(adult_test[predictors])

#Creating dataframe with only the columns Kaggle wants from dataset
submission = pandas.DataFrame({
        "income": predictions
    })

import os
os.remove('entrega.txt')
submission.to_csv('entrega.txt', header=None, index=None, sep=' ', mode='a')

print "Done."

################
