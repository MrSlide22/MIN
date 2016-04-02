import pandas

titanic = pandas.read_csv("train.csv")

print titanic.describe(), "\n"

print "Filling missing data in Age column with median: ", titanic["Age"].median(), "\n"
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

#Converting non-numeric columns (Sex and Embarked)
#Rest of non-numeric columns have been ignored
print "Converting Sex values", titanic["Sex"].unique(), " to numeric values [0, 1]\n"

#Replacing male with 0 and female with 1
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

#Filling and converting Embarked column
print "Filling missing data in Embarked column with 'S'"
titanic["Embarked"] = titanic["Embarked"].fillna("S")
print "Converting Embarked values", titanic["Embarked"].unique(), " to numeric values [0, 1, 2]\n"
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

#On to machine learning
#We'll use linear regression and cross validation
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold

#The columns we'll use to predict the target
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

#Initialize algorithm
alg = LinearRegression()

#Generate cross validation
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

predictions = []
for train, test in kf:
    #Predictors we are using to train the algorithm
    train_predictors = titanic[predictors].iloc[train]
    #Target for training
    train_target = titanic["Survived"].iloc[train]
    #Training algorithm
    alg.fit(train_predictors, train_target)

    #Making predictions on the test fold
    test_predictions = alg.predict(titanic[predictors].iloc[test,:])
    predictions.append(test_predictions)

#Logistic regression to clean up and map predictions to (1, 0)
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
alg = LogisticRegression(random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv = 3)
print "Predictions done with accuracy of: ", scores.mean(), "\n"

#Processing the test set
titanic_test = pandas.read_csv("test.csv")
titanic_test["Age"] = titanic_test["Age"].fillna(titanic_test["Age"].median())
titanic_test["Fare"] = titanic_test["Fare"].fillna(titanic_test["Fare"].median())
titanic_test.loc[titanic_test["Sex"] == "male", "Sex"] = 0
titanic_test.loc[titanic_test["Sex"] == "female", "Sex"] = 1
titanic_test["Embarked"] = titanic_test["Embarked"].fillna("S")
titanic_test.loc[titanic_test["Embarked"] == "S", "Embarked"] = 0
titanic_test.loc[titanic_test["Embarked"] == "C", "Embarked"] = 1
titanic_test.loc[titanic_test["Embarked"] == "Q", "Embarked"] = 2

#Generating submission file
print "Generating submission file..."
alg = LogisticRegression(random_state=1)
alg.fit(titanic[predictors], titanic["Survived"])

predictions = alg.predict(titanic_test[predictors])

#Creating dataframe with only the columns Kaggle wants from dataset
submission = pandas.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": predictions
    })

submission.to_csv("kaggle.csv", index=False)
print "Done."
